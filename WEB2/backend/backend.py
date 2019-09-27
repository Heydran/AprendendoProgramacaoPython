from flask import Flask , jsonify
from playhouse.shortcuts import model_to_dict
from peewee import *

db = SqliteDatabase("slite.db")

class Pessoa(Model):
	nome = CharField()
	class Meta:
		database = db
		

app = Flask (__name__)
@app.route("/")
def inicio () :
	db.connect()
	db.create_tables([Pessoa])
	p = Pessoa.create(nome = "João da Silva")
	m = Pessoa.create(nome = "Maria de Oliveira")
	# forma alternativa rápida: usando map (lambda)
	#pessoas = list(model_to_dict(m))
	pessoas = list(map(model_to_dict, Pessoa.select()))
	return jsonify ({"lista":pessoas }) # refer ência : https :// www.geeksforgeeks.org/python–map–function/

app.run(debug=True, port=4999)