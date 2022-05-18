import flask
from flask import jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json

app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/kommunistisches")
db = mongodb_client.db

@app.route("/add_one")
def add_one():
    db.daily.insert_one({'frase': "Lembre-se: O mundo só é um lugar ruim, pois essa é a forma mais lucrativa de se vender felicidade.", 'dica': "Dica de hoje: não leve garrafa d'água para o trabalho, use um copo pequeno, assim você para de trabalhar mais vezes e ninguém fica te questionando."})
    return json.dumps("Sucesso", default=str)

@app.route("/")
def home():
    holder = list()
    for i in db.daily.find():
        holder.append({'frase':i['frase'], 'dica' : i['dica']})


    return jsonify(holder)