const express = require('express')
const router = express.Router()

router.get('/',(req, res, next) => 
{
    res.status(200).send({
        mensagem: 'Usando o get na rota /produtos'
    })
});

router.post('/', (req, res, next) => 
{
    res.status(201).send({
        mensagem: 'Usando o post na rota/produtos'
    })
});

router.patch('/',(req, res, next)=> {
    res.status(200).send({
        mensagem: 'patch funcionando corretamente'
    })
});

router.delete('/', (req, res, next) => {
    res.status(200).send({
        mensagem: 'estou pronto para deletar esses caraio'
    })
})

router.get('/:id_produto', (req, res, next) => 
{
    const id = req.params.id_produto

    if (id == 'especial')
    {
        res.status(200).send({
            mensagem: 'voce colocou o id ' + id + ' do caralho em'
        })
    }
    else
    {
        res.status(200).send({
            mensagem: 'voce passou um id bem bosta enfia ' + id + ' no seu cu'
        })
    }
})


module.exports = router