//chamando modulos
const express = require('express')
const app = express();
const morgan = require('morgan')
const bodyParser = require('body-parser')

//definindo arquivos
const rotaProdutos = require('./routes/produtos')
const rotaPedidos = require('./routes/pedidos')

//usando modulos
app.use(morgan('dev'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

//tratando o CORS --segurança
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*') 
    //onde * seria o http://servidorQueConsome.com.lugar
    res.header(
        'Access-Control-Allow-Header',
        'Origin, X-Requested-With, content-Type, Accept, Authorization'
    )
    //definindo hearder de entrada de dados
    if (req.method == 'OPTIONS')
    {res.header('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, PUT');
    return res.status(200).send({})}
    next();
})

//rotas, arquivos
app.use('/produtos', rotaProdutos);
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