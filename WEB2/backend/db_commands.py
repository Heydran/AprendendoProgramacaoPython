from peewee_site import *

def cadastrar_usuario():
	Usuario(code = codigo, user = user, passwd = passwd)

db.create_tables([Usuario,])