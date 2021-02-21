const express = require('express')
const router = express.Router()

router.get('/',(req, res, next) => 
{
    res.status(200).send({
        mensagem: 'Usando o get na rota /pedidos'
    })
});

router.post('/', (req, res, next) => 
{
    const pedido = 
    {
        id_produto: req.body.id_produto,
        quantidade: req.body.quantidade
    }
    res.status(201).send({
        mensagem: 'Usando o post na rota/pedidos',
        pedidoCriado: pedido
    })
});


router.delete('/', (req, res, next) => {
    res.status(200).send({
        mensagem: 'estou pronto para deletar esses pedido de pipoca'
    })
})

router.get('/:id_pedido', (req, res, next) => 
{
    const id = req.params.id_pedido
    res.status(200).send({
        mensagem: 'voce colocou o id ' + id
    })
})


module.exports = router