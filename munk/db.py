import json


def insert(model_name, model, file_name='db.json'):
    db = json.load(open(file_name, 'r'))
    table = db['models'][model_name]
    if set(model) != set(table):
        raise ValueError
    db['tables'][model_name][db['sequences'][model_name]] = model
    db['sequences'][model_name] += 1
    json.dump(db, open(file_name, 'w'))

def select(model_name, conditions, file_name='db.json'):
    db = json.load(open(file_name, 'r'))
    if any(condition not in db['models'][model_name] for condition in conditions):
        raise KeyError
    return [model for id, model in db['tables'][model_name].items() if all(model[condition] == value for condition, value in conditions.items())]

def delete(model_name, conditions, file_name='db.json'):
    db = json.load(open(file_name, 'r'))
    if any(condition not in db['models'][model_name] for condition in conditions):
        raise KeyError
    db['tables'][model_name] = {id: model for id, model in db['tables'][model_name].items() if not all(model[condition] == value for condition, value in conditions.items())}
    json.dump(db, open(file_name, 'w'))

def update(model_name, new_values, conditions, file_name='db.json'):
    db = json.load(open(file_name, 'r'))
    if any(condition not in db['models'][model_name] for condition in conditions):
        raise KeyError
    for id, fields in db['tables'][model_name].items():
        if any(fields[condition] != value for condition, value in conditions.items()):
            continue
        for key, value in new_values.items():
            db['tables'][model_name][id][key] = value

    json.dump(db, open(file_name, 'w'))
