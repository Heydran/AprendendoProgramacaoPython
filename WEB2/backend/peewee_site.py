from peewee import *

db = SqliteDatabase("Pessoas.db")

class Model2(Model):
	class Meta:
		database = db

class Usuario(Model2):
	code = AutoField(primary_key = True)
	name = CharField()
	user = CharField()
	passwd = CharField()

db.connect()
db.create_tables([Usuario,])
