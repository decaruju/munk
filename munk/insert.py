import json


def insert(model_name, model, file_name='db.json'):
    db = json.load(open(file_name, 'r'))
    table = db['models'][model_name]
    if set(model) != set(table):
        raise ValueError
    db['tables'][model_name][db['sequences'][model_name]] = model
    db['sequences'][model_name] += 1
    json.dump(db, open(file, 'w'))
