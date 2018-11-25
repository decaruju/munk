import json


class DB:
    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def db(self):
        with open(self.file_name, 'r') as file:
            data = json.load(file)
        return data

    @db.setter
    def db(self, db):
        with open(self.file_name, 'w') as file:
            json.dump(db, file)

    def insert(self, model_name, model):
        db = self.db
        table = db['models'][model_name]
        if set(model) != set(table):
            raise ValueError
        db['tables'][model_name][db['sequences'][model_name]] = model
        for field, value in model.items():
            if db['models'][model_name][field]['index']:
                db['indexes'][model_name][field].setdefault(value, []).append(str(db['sequences'][model_name]))
        db['sequences'][model_name] += 1
        self.db = db

    def select(self, model_name, conditions={}, file_name='db.json'):
        db = self.db
        if any(condition not in db['models'][model_name] for condition in conditions):
            raise KeyError
        ids = set(db['tables'][model_name])
        for field, value in conditions.items():
            if db['models'][model_name][field]['index']:
                ids &= set(db['indexes'][model_name][field][value])
            else:
                ids = {id for id in ids if db['tables'][model_name][id][field] == value}

        return [db['tables'][model_name][id] for id in ids]

    def delete(self, model_name, conditions={}, file_name='db.json'):
        db = self.db
        if any(condition not in db['models'][model_name] for condition in conditions):
            raise KeyError
        db['tables'][model_name] = {id: model for id, model in db['tables'][model_name].items() if not all(model[condition] == value for condition, value in conditions.items())}
        self.db = db

    def update(self, model_name, new_values, conditions={}, file_name='db.json'):
        db = self.db
        if any(condition not in db['models'][model_name] for condition in conditions):
            raise KeyError
        for id, fields in db['tables'][model_name].items():
            if any(fields[condition] != value for condition, value in conditions.items()):
                continue
            for key, value in new_values.items():
                db['tables'][model_name][id][key] = value
        self.db = db
