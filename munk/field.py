class Field:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.index = kwargs.get('index', False)
        self.to = kwargs.get('to', None)

    def __str__(self):
        return str(self.type)

    def dict(self):
        return {'type': self.type, 'index': self.index, 'to': self.to}

    __repr__ = __str__
