from peewee import *


arq = "./database.db"
db = SqliteDatabase(arq)

class Modelo(Model):
	class Meta:
		database = db

class Anime(Modelo):
	nome = CharField()
	genero = CharField()

if __name__ == '__main__':
	import random
	db.connect()
	db.create_tables([Anime])
	generos = ["ação", "comédia", "aventura","sekai"]
	Anime(nome = ("anime"+str(random.randint(0,9999))), genero =generos[random.randint(0,3)] ).save()
	for i in Anime.select():
		print(i.nome, i.genero)