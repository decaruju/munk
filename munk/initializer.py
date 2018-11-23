import yaml
import pickle
from model import Model


with open('db.yaml') as file:
    data = yaml.load(file.read())


models = {model: Model(fields) for model, fields in data.items()}


pickle.dump(models, open('db.pkl'))
