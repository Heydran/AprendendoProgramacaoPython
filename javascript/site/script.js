$("#btn_listar_animes").click(function(){
	$.ajax({
		url: 'http://localhost:5000/listar_animes',
		method: 'GET',
		dataType: 'json',
		success: function(resultado){
			$("tabela_animes").empty()
			pessoas = resultado.lista;
			var cabecalho = '<div class="rTableRow">' +
			    '<div class="rTableHead">Nome</div>' +
                '<div class="rTableHead">Genero</div>' +
                '</div>';
           	$("#tabela_animes").append(cabecalho)
           	for (var in pessoas){
           		$("#tabela_animes").append(formatar_pessoa_tabela(pessoas[i]))
           	}
		},
		error: function(argument) {
			alert("error")
		}
	});
});