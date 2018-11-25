import yaml

from .db import DB


def seed_db(seed_file_name, db_file_name):
    with open(seed_file_name, 'r') as file:
        seed = yaml.load(file)

    db = DB(db_file_name)

    for model_name, fields in seed.items():
        model = fields['model']
        del fields['model']
        db.insert(model, fields)
