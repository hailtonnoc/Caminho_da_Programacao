var botao = document.querySelector('#salvar')
botao.addEventListener('click', function(event)
{
    event.preventDefault()

//pegar valor dos elementos
var form = document.querySelector('.entrada')
//                 name do input
var produto = form.produto.value;
var quantidade = form.quantidade.value;
var unidade = form.vunidade.value;

//criar elementos
var produtoTr = document.createElement("tr")

var produtoTd = document.createElement("td")
var quantidadeTd = document.createElement("td")
var unidadeTd = document.createElement("td")
var totalTd = document.createElement("td")

produtoTd.textContent = produto
quantidadeTd.textContent = quantidade
unidadeTd.textContent = unidade
totalTd.textContent = calculoTotal(quantidade, unidade)

produtoTr.appendChild(produtoTd)
produtoTr.appendChild(quantidadeTd)
produtoTr.appendChild(unidadeTd)
produtoTr.appendChild(totalTd)

var tabela = document.querySelector('.corpoTabela')
tabela.appendChild(produtoTr)

}
)