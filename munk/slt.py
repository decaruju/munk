import json


def slt(model_name, conditions, file_name='db.json'):
    db = json.load(open(file_name, 'r'))
    if any(condition not in db['models'][model_name] for condition in conditions):
        raise KeyError
    return [db['tables'][model_name][model] for model in db['tables'][model_name] if all(model['condition'] == value for condition, value in conditions)]
