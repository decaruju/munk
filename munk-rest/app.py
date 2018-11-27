from flask import Flask, request
from munk import DB, initializer, seed
import os


app = Flask(__name__)

@app.route('/<user>/<project>/<path:query>/')
def main(user, project, query):
    db_path = os.path.join(user, project + '.json')
    print(db_path)
    if not os.path.exists(db_path):
        os.mkdir(user)
    db = DB(db_path)
    models, comps, params = parse_query(query)
    return str(db.select(models[0], comps))

def parse_query(query_string):
    args = query_string.split('/')

    models = args[0] if len(args) >= 1 else ''
    comps = args[1] if len(args) >= 2 else ''
    params = args[2] if len(args) >= 3 else ''

    models = models.split('&')
    if len(comps) > 0:
        comps = {arg.split('=')[0]: arg.split('=')[1] for arg in comps.split('&')}
    else:
        comps = {}
    params = params.split('&')

    return models, comps, params



    
