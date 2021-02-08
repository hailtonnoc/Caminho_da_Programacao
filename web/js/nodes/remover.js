/*var produtos = document.querySelectorAll('.produto')
produtos.forEach(function(produto)
{
    produto.addEventListener('click', function()
    {
        this.remove()
    }
    )
}
)*/

var tabela = document.querySelector('.corpoTabela')

tabela.addEventListener('dblclick', function(event)
{
    var alvo = event.target
    var paiAlvo = alvo.parentNode
    paiAlvo.remove()
})