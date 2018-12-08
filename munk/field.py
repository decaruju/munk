class Field:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.index = kwargs.get('index', False)
        self.to = kwargs.get('to', None)
        self.required = kwargs.get('required', False)

    def __str__(self):
        return str(self.type)

    def dict(self):
        return {'type': self.type, 'index': self.index, 'to': self.to, 'required': self.required}

    __repr__ = __str__
