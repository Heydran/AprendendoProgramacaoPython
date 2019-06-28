'''

Considere um sistema que armazene informações de uma marcenaria. Deseja-se registrar as
mobílias (novas/a serem construídas sob medida, ou já disponíveis para venda), os materiais
utilizados, bem como os pedidos dos clientes. Um pedido pode conter uma ou mais mobílias.
Deseja-se também registrar o estoque de material disponível. Liste as classes e os atributos
necessários para armazenar essas informações da melhor maneira possível.

'''

from peewee import *

db = SqliteDatabase("marcenaria")

class MM(Model):
	class Meta:
		database = db

class Mobilia(MM):
	cod_mobilia = AutoField(primary_key = True)
	den_mobilia = CharField()
	tipo_mobilia = CharField()
	material = CharField()
	qnt_material = CharField()

class Estoque(MM):
	cod_material = AutoField(primary_key = True)
	den_material = CharField()
	qnt_material = CharField()

class Pedido(MM):
	cod_pedidio = AutoField(primary_key = True)
	mobilias = ManyToManyField(Mobilia)

class TrinaryField(CharField):
        def db_value(self, value):
            if value not in ["Encomendada","Disponivel"]:
                raise TypeError("Non-trinary digit")
            return super().db_field(value)

if __name__ == '__main__':
	db.connect()
	db.create_tables([Mobilia, Estoque, Pedido.mobilias.get_through_model()])

	m1 = Mobilia(den_mobilia = "Estante", tipo_mobilia = "Encomendada", material = "Madeira", qnt_material = "10m²").save()
	p1 = Mobilia.select().where(Mobilia.cod_mobilia == 1)
	print(p1)
	for i in p1: print(i)