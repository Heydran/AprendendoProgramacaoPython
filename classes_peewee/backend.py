from flask import Flask, json, jsonify
from flask import request
from playhouse.shortcuts import model_to_dict
from classes_peewee import *

app = Flask(__name__)

@app.route('/pedir_albuns')
def pedir_albuns():
	albuns = list(map(model_to_dict, Album.select()))
	response = jsonify({"lista": albuns})
	response.headers.add("Acess-Controll-Allow_Origin","*")
	return response
app.run(debug = True)