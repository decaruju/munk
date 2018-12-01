import json

from .field import Field


class Model:
    def __init__(self, fields):
        self.fields = {name: Field(**desc) for name, desc in fields.items()}

    def __str__(self):
        return str(self.fields)

    def dict(self):
        return {name: field.dict() for name, field in self.fields.items()}

    __repr__ = __str__
