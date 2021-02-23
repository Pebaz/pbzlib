"""
Simple AWS SQS Service.
"""

import json, boto3
from typing import *


class SimpleSqsService:
    "Dictionary-only API, no Pydantic models"

    def __init__(self, queue_url: str):
        self.queue = boto3.resource('sqs').Queue(queue_url)
    
    def deserialize_attributes(self, attributes: dict) -> dict:
        "Turns stringified attributes back into their actual data type."
        return {
            key: json.loads(value['StringValue'])
            for key, value in attributes.items()
        }

    def serialize_attributes(self, attributes: dict) -> dict:
        "Turns attributes dict into valid SQS attribute dict."
        return {
            attr_name: {
                'DataType': 'String',
                'StringValue': json.dumps(attr_value)
            }
            for attr_name, attr_value in attributes.items()
        }

    def send_message(
        self,
        message: dict,
        attributes: Optional[dict] = None
    ) -> None:
        try:
            command = dict(MessageBody=json.dumps(message))

            if attributes:
                command['MessageAttributes'] = self.serialize_attributes(
                    attributes
                )
            
            self.queue.send_message(**command)
        except Exception as e:
            raise Exception(f'Failed to send message({message}): {e}') from e

    def read_message(self) -> dict:
        try:
            response = self.queue.receive_messages(
                MaxNumberOfMessages=1,
                AttributeNames=[],
                MessageAttributeNames=['*']
            )

            if response:
                message = response[0]

                return {
                    'id': message.message_id,
                    'handle': message.receipt_handle,
                    'body': json.loads(message.body),
                    'attributes': self.deserialize_attributes(
                        message.message_attributes
                    )
                }
        except Exception as e:
            raise Exception(f'Failed to read message from queue: {e}') from e

    def delete_message(self, msg_id: str, msg_handle: str) -> None:
        response = {}

        try:
            response = self.queue.delete_messages(
                Entries=[dict(Id=msg_id, ReceiptHandle=msg_handle)]
            )
        except Exception as e:
            raise Exception(f'Failed to delete message({msg_id}): {e}') from e

        if 'Failed' in response:
            raise Exception(f'Failed to delete message({msg_id}): {e}') from e
