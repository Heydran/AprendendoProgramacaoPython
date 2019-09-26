from flask import Flask, render_template, request, redirect, session
from db_commands import *

app = Flask("__name__")
app.secret_key = 'senha'

@app.route("/cadastrar_usuario")
def cadastrar_usuario():
	user = resquest.args.get("user")
	passwd = resquest.args.get("passwd")
	name = resquest.args.get("name")
	cadastrar_usuario()
	return True

app.run(debug=True, host = "4999")