from peewee import *

db = SqliteDatabase("Mercado.db")

class MM(Model):
	class Meta:
		database = db

class Carrinho(MM):
	cod_carrinho = CharField(primary_key = True)

class Produto(MM):
	cod_produto = CharField(primary_key = True)

class Compra(MM):
	cod_carrinho = ForeignKeyField(Carrinho)
	cod_produto = ForeignKeyField(Produto)