var botao = document.querySelector('#salvar')
botao.addEventListener('click', function(event)
{
    event.preventDefault()

//pegar valor dos elementos
var form = document.querySelector('.entrada')
/*
extraindo informações
var produto = form.produto.value;
var quantidade = form.quantidade.value;
var unidade = form.vunidade.value;
*/
var produto = obtemProdutoEstoque(form)
console.log(produto)

/*Substituído por montarTr
criar elementos
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
*/
var produtoTr = montarTr(produto)

//adicionando na pagina
var tabela = document.querySelector('.corpoTabela')
tabela.appendChild(produtoTr)

form.reset()
}
)

function obtemProdutoEstoque(form)
{
    var produto = 
    {
        nome: form.produto.value,
        quantidade: form.quantidade.value,
        valorUnitario: form.vunidade.value,
        total: calculoTotal(form.quantidade.value, form.vunidade.value)
    }

    return produto //return importante
}

function montarTr(produto)
{
    var produtoTr = document.createElement("tr")
    produtoTr.classList.add('produto')
    /*subistituido por montaTd
    var produtoTd = document.createElement("td")
    var quantidadeTd = document.createElement("td")
    var unidadeTd = document.createElement("td")
    var totalTd = document.createElement("td")

    produtoTd.textContent = produto.nome
    quantidadeTd.textContent = produto.quantidade
    unidadeTd.textContent = produto.valorUnitario
    totalTd.textContent = produto.total
    */
    var produtoTd = montaTd(produto.nome, 'info-nome')
    var quantidadeTd = montaTd(produto.quantidade, 'info-estoque')
    var unidadeTd = montaTd(produto.valorUnitario, 'info-unidade')
    var totalTd = montaTd(produto.total, 'info-total')


    produtoTr.appendChild(produtoTd)
    produtoTr.appendChild(quantidadeTd)
    produtoTr.appendChild(unidadeTd)
    produtoTr.appendChild(totalTd)

    return produtoTr //ta vendo
}

function montaTd(dado, classe)
{
    var td = document.createElement('td')
    td.textContent = dado
    td.classList.add(classe)

    return td
}