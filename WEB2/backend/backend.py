from flask import Flask, jsonify, session
import requests
from playhouse.shortcuts import model_to_dict
from peewee import *

db = SqliteDatabase("slite.db")
class Pessoa(Model):
	nome = CharField()
	class Meta:
		database = db
		
db.connect()
db.create_tables([Pessoa])

app = Flask (__name__)
app.secret_key = 'senha'

@app.route("/listar_pessoas")
def listar_pessoas():
	pessoas = list(map(model_to_dict, Pessoa.select()))
	return jsonify({"pessoas":pessoas})

@app.route("/cadastrar_pessoa")
def cadastrar_pessoas():
	pessoa = requests.get("http://localhost:5000/info_cadastro_pessoa")
	json_pessoa = pessoa.json()
	Pessoa.create(nome = json_pessoa["name"])
	return jsonify({"cadastrado":json_pessoa["name"]})

app.run(debug=True, port=4999)
