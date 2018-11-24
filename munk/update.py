import json


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

