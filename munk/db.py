import json
from datetime import datetime

def reference(id):
    return str(id)

TYPES = {'str': str, 'int': int, 'float': float, 'bool': bool, 'reference': reference, 'datetime': str}

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
        if not set(model) <= set(db['models'][model_name]):
            raise ValueError(f'{model} and {db["models"][model_name]}')
        for field, value in model.items():
            model[field] = TYPES[db['models'][model_name][field]['type']](value)

        db['tables'][model_name][db['sequences'][model_name]] = model
        for field, value in model.items():
            if db['models'][model_name][field]['index']:
                db['indexes'][model_name][field].setdefault(value, []).append(str(db['sequences'][model_name]))
        db['sequences'][model_name] += 1
        self.db = db

    def select(self, model_name, conditions={}):
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

    def join(self, field_name, objects, model_name, conditions={}):
        db = self.db

        for item in objects:
            field_model = db['models'][model_name][field_name]['to']
            item[field_name] = {key: db['tables'][field_model][str(key)] for key in list(item[field_name])}
        return objects


    def delete(self, model_name, conditions={}):
        db = self.db
        if any(condition not in db['models'][model_name] for condition in conditions):
            raise KeyError
        for field, attrs in db['models'][model_name].items():
            if attrs['index']:
                for id, model in db['tables'][model_name].items():
                    if all(model[condition] == value for condition, value in conditions.items()):
                        db['indexes'][model_name][field][model[field]].remove(id)
                    if len(db['indexes'][model_name][field][model[field]]) == 0:
                        del db['indexes'][model_name][field][model[field]]
        db['tables'][model_name] = {id: model for id, model in db['tables'][model_name].items() if not all(model[condition] == value for condition, value in conditions.items())}
        self.db = db

    def update(self, model_name, new_values, conditions={}):
        db = self.db
        if any(condition not in db['models'][model_name] for condition in conditions):
            raise KeyError
        for id, fields in db['tables'][model_name].items():
            if any(fields[condition] != value for condition, value in conditions.items()):
                continue
            for key, value in new_values.items():
                if db['models'][model_name][key]['index']:
                    db['indexes'][model_name][key][fields[key]].remove(id)
                    breakpoint()
                    if len(db['indexes'][model_name][key][fields[key]]) == 0:
                        del db['indexes'][model_name][key][fields[key]]
                    db['indexes'][model_name][key].setdefault(value, []).append(id)
                db['tables'][model_name][id][key] = value
        self.db = db
