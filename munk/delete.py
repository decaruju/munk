import json


def delete(model_name, conditions, file_name='db.json'):
    db = json.load(open(file_name, 'r'))
    if any(condition not in db['models'][model_name] for condition in conditions):
        raise KeyError
    db['tables'][model_name] = {id: model for id, model in db['tables'][model_name].items() if not all(model[condition] == value for condition, value in conditions.items())}
    json.dump(db, open(file_name, 'w'))
