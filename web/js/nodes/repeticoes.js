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





