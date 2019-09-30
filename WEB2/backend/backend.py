from flask import Flask, jsonify, session, request
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

@app.route("/")
def oi():
	return "oi"

@app.route("/listar_pessoas")
def listar_pessoas():
	pessoas = list(map(model_to_dict, Pessoa.select()))
	return jsonify({"pessoas":pessoas})

@app.route("/cadastrar_pessoa")
def cadastrar_pessoas():
	nome = request.args.get("nome")
	Pessoa.create(nome = nome)
	return jsonify({"cadastrado":nome})

app.run(debug=True, port=4999, host = "0.0.0.0")