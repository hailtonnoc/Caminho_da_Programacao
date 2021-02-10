const Atendimento = require('../models/atendimentos')

module.exports = app =>
{
    app.get('/atendimento', function(req, res)
    {
        res.send('servidor dedicado a cadastro de atendimentos! e isso foi inputado utilizando um GET')
    })

    app.post('/atendimento', (req, res) => 
    {
        const atendimento = req.body

        Atendimento.adiciona(atendimento, res)
    })
}
