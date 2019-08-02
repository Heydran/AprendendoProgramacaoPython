from peewee import *

db = SqliteDatabase("Receitas")

class Modelo(Model):
	class Meta:
		database = db

class Receita(Modelo):
	cod_receita = AutoField(primary_key = True)
	nom_receita = CharField()

class Ingrediente(Modelo):
	cod_ingrediente = AutoField(primary_key = True)
	nom_ingrediente = CharField()

class IngredientesReceita(Modelo):
	receita = ForeignKeyField(Receita)
	ingrediente = ForeignKeyField(Ingrediente)
	quantidade = CharField()


if __name__ == '__main__':
	db.connect()
	db.create_tables([Receita, Ingrediente, IngredientesReceita])
	#r1 = Receita(nom_receita = "Bolo").save()
	#i1 = Ingrediente(nom_ingrediente = "Farinha").save()
	#ir1 = IngredientesReceita(receita = 1, ingrediente = 1, quantidade = 2).save()
	rec = Receita.get_by_id(1)
	lista_de_receitas = IngredientesReceita\
	.select()\
	.where(IngredientesReceita.receita == rec)
	for i in lista_de_receitas:
		print(i.ingrediente.nom_ingrediente)