from field import Field


class Model:
    def __init__(self, fields):
        self.fields = {name: Field(**desc) for name, desc in fields.items()}

    def __str__(self):
        return str(self.fields)

    __repr__ = __str__
