from flask import Flask , render_template
import requests
from playhouse. shortcuts import dict_to_model
from peewee import *

db = SqliteDatabase(":memory:")

class Pessoa(Model):
	nome = CharField()
	class Meta:
		database = db
		

app = Flask (__name__)
@app.route("/")
def inicio () :
	dados_pessoas = requests . get("http://localhost:4999/")
	json_pessoas = dados_pessoas.json()
	pessoas = []
	for pessoa_em_json in json_pessoas["lista"]:
		p = dict_to_model(Pessoa, pessoa_em_json)
		pessoas.append(p)
	return render_template("listar_pessoas.html", lista = pessoas)

app.run(debug=True)