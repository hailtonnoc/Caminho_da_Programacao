const express = require('express')
const app = express();

const rotaProdutos = require('./routes/produtos')

app.use('/produtos', rotaProdutos);

app.use('/caminho',(req, res, next) => 
{
    res.status(200).send({
        mensagem: 'OK, TUDO NA MESMA PORRA'
    });
});

module.exports = app;