var produto = document.querySelector(".produto1")

var estoque = produto.querySelector('.info-estoque')
var estq = estoque.textContent
var vUnitario = produto.querySelector('.info-unidade')
var unid = vUnitario.textContent

var vTotal = produto.querySelector(".info-total")

var total = estq * unid

vTotal.textContent = total

console.log(estq)
console.log(unid)
console.log(total)