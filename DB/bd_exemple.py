from peewee import *

db = SqliteDatabase('Manga.db')

class Genero(Model):
	cod_genero = AutoField(primary_key = True)		
	den_genero = CharField()
	class Meta:
		database = db

class Manga(Model):
	cod_manga = AutoField(primary_key = True)
	titulo = CharField()
	genero = ForeignKeyField(Genero)
	class Meta:
		database = db
	def __str__(self):
		return 'codigo: ' + str(self.cod_manga) + ' - titulo: ' + self.titulo + ' - genero: ' + self.genero
	

if __name__ == '__main__':
	try:
		db.connect()
		db.create_tables([Manga,])
	except Exception as e:
		raise e

	o1 = Genero()

	o2 = Manga(titulo = "solo leveling", genero = "ação")
	print(o)

	o.save()

	t = Manga.select()

	for i in t:
		print(i)
	
