import yaml
import json
from model import Model



with open('examples/db.yaml') as file:
    data = yaml.load(file.read())
    
    
    
models = {model: Model(fields).dict() for model, fields in data.items()}

json.dump({
        'models': models,
        'tables': {model: {} for model in models},
        'sequences': {model: 0 for model in models},
        'indexes': {model_name: {field: {} for field, attrs in model.items() if attrs['index']} for model_name, model in models.items()},
}, open('examples/db.yaml', 'w'))
