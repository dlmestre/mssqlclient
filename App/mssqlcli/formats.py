import json
import datetime
import uuid


class FormatException(Exception):
    pass


class Formatter:

    def __new__(cls, option: str, data: list, plain: bool):
        _formats = {'json': Formatter._json}
        _format = _formats.get(option)
        if _format:
            return _format(data, plain)
        else:
            raise FormatException('format not defined')

    @staticmethod
    def _json(data: str, plain: bool) -> str:
        if plain:
            return json.dumps(Formatter._string(data), indent=4)
        return json.dumps(Formatter._string({'data': data}), indent=4)

    @staticmethod
    def _string(content: any) -> any:
        iterable = Formatter._iterable(content)
        for key, value in iterable:
            if type(value) == datetime.datetime:
                content[key] = str(value)

            if type(value) == uuid.UUID:
                content[key] = str(value)

            if type(value) in [list, dict]:
                content[key] = Formatter._string(value)
        return content

    @staticmethod
    def _iterable(content: any) -> any:
        if type(content) == list:
            return enumerate(content)
        if type(content) == dict:
            return content.items()
        raise FormatException('content is not of type list or dict')
