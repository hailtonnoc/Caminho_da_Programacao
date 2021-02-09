module.exports = app =>
{
    app.get('/atendimento', function(req, res)
    {
        res.send('servidor dedicado a cadastro de atendimentos! e isso foi inputado utilizando um GET')
    })

    app.post('/atendimento', (req, res) => 
    {
        console.log(req.body)
        res.send('rota de atendimentos e realizando um post')
    })
}
