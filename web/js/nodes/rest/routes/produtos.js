const express = require('express')
const router = express.Router()
const mysql = require('../mysql').pool;

router.get('/',(req, res, next) => 
{
    mysql.getConnection((error, conn) => {
        if(error) {return res.status(500).send({error: error})}

        conn.query(
            'SELECT * FROM produtos;',
            (error, resultado, fields) => {
                if(error) {return res.status(500).send({error: error})}
                return res.status(200).send({response: resultado})
            }
            )
    })
});

router.post('/', (req, res, next) => {

    mysql.getConnection((error, conn) => {
        conn.query(
            'INSERT INTO produtos (nome, preco) VALUES (?,?)',
            [req.body.nome, req.body.preco],
            (error, resultado, field) => {
            conn.release();
            if(error){
                return res.status(500).send({
                    error: error,
                    response: null
                });
            }
            res.status(201).send({
                mensagem: 'Produto inserido',
                id_produto: resultado.insertId,
                aviso: 'carallho'
            });
        }
    )
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