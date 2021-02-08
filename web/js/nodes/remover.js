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
    event.target.parentNode.classList.add('fadeOut')

    setTimeout(function()
    {
        event.target.parentNode.remove()
    },500)
})