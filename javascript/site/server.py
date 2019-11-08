from flask import Flask, json, jsonify
from flask import request
from modelo import Anime
from playhouse.shortcuts import model_to_dict

# inicializa o servidor
app = Flask(__name__)

@app.route('/listar_animes')
def listar_animes():
	animes = list(map(model_to_dict, Anime.select()))
	response = jsonify({"lista": animes})
	response.headers.add("Acess-Controll-Allow_Origin","*")
	return response
app.run(debug = True)