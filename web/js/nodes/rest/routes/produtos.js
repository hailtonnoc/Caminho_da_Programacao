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
            if(error){return res.status(500).send({error: error})}

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
    mysql.getConnection((error, conn) => {
        conn.query(
            `UPDATE produtos 
            SET nome =?, preco =? 
            WHERE id_produto =?`,
            [req.body.nome, req.body.preco,
            req.body.id_produto],

            (error, resultado, field) => {
            conn.release();
            if(error){return res.status(500).send({error: error})}
            
            res.status(202).send({
                mensagem: 'Produto Alterado'
            });
        }
    )
    })
});

router.delete('/', (req, res, next) => {
    mysql.getConnection((error, conn)=>
    {
        if(error){return res.status(500).send({erro: error})}
        conn.query(
            'DELETE FROM produtos WHERE id_produto = ?;',
            [req.body.id_produto],
            (error, resultado, field)=>
            {
                if(error){return res.status(500).send({erro: error})}
                res.status(202).send({
                    mensagem: 'Produto deletado'
                })
            }
        )
    }
    )
})

router.get('/:id_produto', (req, res, next) => 
{
    mysql.getConnection((error, conn) => {
        if(error){return res.status(500).send({error: error + ' Se fudeu'})}

        conn.query(
            'SELECT * FROM produtos WHERE id_produto = ?;',
            [req.params.id_produto],
            (error, resultado, fields) => 
            {
                if(error){return res.status(500).send({ error: error + 'sifudeu'})}
                return res.status(200).send({response: resultado})
            }
            )
    })
})


module.exports = router