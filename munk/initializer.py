import yaml
import json

from .model import Model


def initialize_db(db_file_name, yaml_file_name):
    with open(yaml_file_name) as file:
        data = yaml.load(file)


    models = {model: Model(fields).dict() for model, fields in data.items()}


    json.dump({
        'models': models,
        'tables': {model: {} for model in models},
        'sequences': {model: 0 for model in models},
        'indexes': {model_name: {field: {} for field, attrs in model.items() if attrs['index']} for model_name, model in models.items()},
    }, open(db_file_name, 'w'))
