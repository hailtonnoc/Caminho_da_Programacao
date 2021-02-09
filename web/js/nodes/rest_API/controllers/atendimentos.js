module.exports = app =>
{
    app.get('/atendimento', function(req, res)
    {
        res.send('servidor dedicado a cadastro de atendimentos! e isso foi inputado utilizando um GET')
    })
}
