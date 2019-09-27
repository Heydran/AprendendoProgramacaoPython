from flask import Flask, render_template, session, request, jsonify
import requests
from playhouse. shortcuts import dict_to_model
from peewee import *

db = SqliteDatabase(":memory:")

class Pessoa(Model):
	nome = CharField()
	class Meta:
		database = db
		

app = Flask (__name__)
app.secret_key = 'senha'

@app.route("/")
def inicio ():
	return render_template("home.html")

@app.route("/listar_pessoas")
def listar_pessoas():
	dados_pessoas = requests.get("http://localhost:4999/listar_pessoas")
	json_pessoas = dados_pessoas.json()
	pessoas = []
	for pessoa_em_json in json_pessoas["pessoas"]:
		p = dict_to_model(Pessoa, pessoa_em_json)
		pessoas.append(p)
	return render_template("listar_pessoas.html", pessoas = pessoas)

@app.route("/form_cadastrar_pessoa")
def form_cadastrar_usuario():
	return render_template("form_cadastrar_pessoa.html")

@app.route("/cadastrar_pessoa")
def cadastrar_pessoa():
	session["form_cadastrar_name"] = request.args.get("name")
	cadastrado = requests.get("http://localhost:4999/cadastrar_pessoa")
	cadastrado_json = cadastrado.json()
	return 	cadastrado_json["cadastrado"]

@app.route("/info_cadastro_pessoa")
def info_cadastro_pessoa():
	return jsonify(name = session["form_cadastrar_name"])

app.run(debug=True)