class Modelo

class Episodio{
	nome: char
	duracao: char
	numero: char
	arquivo: char
}
	
class Genero{
	nome: char
	descricao: char
}

class Personagem{
	nome: char
	idade: char
}

class Produto{
	nome: char
	data: char
	generos: list
	personagens: list
	episodios: list
}

class Anime{
	nome: char
	produto: char
}

class Diretor{
	nome: char
	cpf: char
	salario: char
	projetos: list
}

class Estudio{
	nome: char
	diretor: list 
	animes: list
}

class Filme{
	produto: list
	estudio: list
}

class Usuario{
	nome: char
}

class Album{
	nome: char
	criador: list
	animes: list
	filmes: list
}

Modelo <|-down- Episodio
Modelo <|-down- Genero
Modelo <|-down- Personagem
Modelo <|-down- Produto
Modelo <|-down- Anime
Modelo <|-up- Diretor
Modelo <|-up- Estudio
Modelo <|-up- Filme
Modelo <|-up- Usuario
Modelo <|-up- Album

Produto <|- "many" Genero: generos
Produto <|- "many" Personagem: personagens
Produto <|- "many" Episodio: episodios

Anime  <|- "obj" Produto: produto

Diretor <|- "many" Projeto: projetos

Estudio  <|- "obj" Diretor: diretor
Estudio <|- "many" Anime: animes

Filme <|- "obj" Produto: produto
Filme <|- "obg" Estudio: estudio

Album <|- "obg" Usuario: criador
Album <|- "many" Anime: animes
Album <|- "many" Filme: filmes
