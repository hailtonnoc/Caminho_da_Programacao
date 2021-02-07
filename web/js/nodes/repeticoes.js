//selecionando elemento geral
var produtos = document.querySelectorAll(".produto")

for(var i = 0; i < produtos.length ; i++)
{
    var produto = produtos[i]
    
    //selecionando sub-elementos
    var estoque = produto.querySelector('.info-estoque')
    var estq = estoque.textContent
    var vUnitario = produto.querySelector('.info-unidade')
    var unid = vUnitario.textContent

    var vTotal = produto.querySelector(".info-total")


    //função
    var temEstoque = true
    var temValorUni = true

    if(estq <= 0)
    {
        temEstoque = false 
        vTotal.textContent = "Estoque invalido"
    }

    if(unid <= 0)
    {
        temValorUni = false
        vTotal.textContent = "Valor unitário invalido"
    }

    if(temEstoque && temValorUni)
    {
        var total = estq * unid
        vTotal.textContent = total
    }
}

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

produtoTr.appendChild(produtoTd)
produtoTr.appendChild(quantidadeTd)
produtoTr.appendChild(unidadeTd)
produtoTr.appendChild(totalTd)

var tabela = document.querySelector('.corpoTabela')
tabela.appendChild(produtoTr)

}
)
