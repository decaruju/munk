class Field:
    def __init__(self, **kwargs):
        self.type = kwargs['type']

    def __str__(self):
        return str(self.type)

    def dict(self):
        return {'type': self.type}

    __repr__ = __str__
