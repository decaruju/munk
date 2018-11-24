import yaml
from insert import insert


with open('seed.yaml', 'r') as file:
    db = yaml.load(file.read())

for model_name, fields in db.items():
    model = fields['model']
    del fields['model']
    insert(model, fields)
