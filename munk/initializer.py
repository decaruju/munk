import yaml
import json
from model import Model


with open('examples/db.yaml') as file:
    data = yaml.load(file.read())


models = {model: Model(fields).dict() for model, fields in data.items()}


json.dump({
    'models': models,
    'tables': {model: {} for model in models},
    'sequences': {model: 0 for model in models}
}, open('examples/db.json', 'w'))
