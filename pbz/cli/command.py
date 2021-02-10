"""
* Command names must start with "cmd_"
* Command classes must be all lower snake case
"""

from typing iport list


ArgList = List[str]  # Saves an import for all subclasses


class Command:
    def execute(self, args: ArgList) -> None:
        ...
