from peewee import *

db = SqliteDatabase("Pessoas.db")

class MM(Model):
	class Meta:
		database = db

class Pessoa(MM):
	nom_pessoa = CharField()
	endereco = CharField()

class Contas(MM):
	user = CharField()
	passwd = CharField()