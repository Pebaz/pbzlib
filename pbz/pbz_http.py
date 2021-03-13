"""
It is sometimes preferable to not package requests since it relies on Chardet
and other large packages that take up megabyte of space. The standard library
contains all that is necessary to make HTTP requests. This module simply unlocks
it and makes that functionality easier to use.
"""

try:
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    import warnings
    warnings.warn('Something\'s up.')


class HttpRequest:
    def __init__(
        self,
        url,
        method='GET',
        headers={},
        params={},
        payload=None,
        stream=False,
        decode='UTF-8'  # Can be None to cancel any decoding
    ):
        self.decode = decode
        url_params = urlencode(params)
        self.request = urlopen(
            Request(
                f'{url}?{url_params}',
                headers=headers,
                data=payload
            )
        )

        if not self.stream:
            "Complete the request now and store the data"
    
    def read(self, num_bytes):
        """
        Available to make this request adhere to the file protocol.
        Can be passed to file readers to stream data.
        """
        try:
            data = self.request.read(num_bytes)
            if self.decode:
                return data.decode(self.decode)
            else:
                return data
        except StopIteration:
            # TODO(pebaz): Support b'' and '' ('rb' and 'r')
            return ''

    def json(self):
        "json.loads(self.request.content())"
