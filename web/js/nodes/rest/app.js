const express = require('express')
const app = express();
const morgan = require('morgan')
app.use(morgan('dev'))

const rotaProdutos = require('./routes/produtos')
app.use('/produtos', rotaProdutos);

const rotaPedidos = require('./routes/pedidos')
app.use('/pedidos', rotaPedidos);



//aprendendo rotas
app.use('/caminho',(req, res, next) => 
{
    res.status(200).send({
        mensagem: 'OK, TUDO CERTO, CAMINHO É O CAMINHO E `RES` É A RESPOSTA ATRAVES DO .SEND'
    });
});

//caso rota não encontrada
app.use((req, res, next) => {
    const erro = new Error('não encontrado');
    erro.status = 404;
    next(erro);
})
app.use((error, req, res, next) =>{
    res.status(error.status || 500);
    return res.send({
        erro:
        {mensagem:error.message}
    })
})




module.exports = app;