class pessoa
{
    nome;
    cpf;
    nascimento;
}

const pessoa1 = new pessoa()

    pessoa1.nome = "Hailton";
    pessoa1.cpf = "4504807209";
    pessoa1.nascimento = "25/04/1996"

var moldeclass = document.getElementById('moldeclass')
moldeclass.innerText = `O CPF do ${pessoa1.nome} é o ${pessoa1.cpf}`


class conta
{
    corretora;
    tipodeinvestimento;
    saldo;
    nivel;

    sacar(valor)
    {
        if (this.saldo >= valor)
        {this.saldo -= valor}
    }
    depositar(valor)
    {
        if(valor >= 0)
        {this.saldo += valor}
    }
}

const conta1 = new conta()

conta1.corretora = "NocsInvesting";
conta1.tipodeinvestimento = "Meercado de Ações"
conta1.saldo = 999.99
conta1.nivel = "tranquileba"

var objeto = document.getElementById('objeto')
objeto.innerHTML = `A conta de ${pessoa1.nome} tem atualmente R&#36; ${conta1.saldo}`

conta1.sacar(9)
conta1.depositar(9000)
objetof.innerHTML = `A conta de ${pessoa1.nome} tem atualmente R&#36; ${conta1.saldo}`

var inseguranca = document.getElementById('inseguranca')
conta1.saldo = 180000
inseguranca.innerText = `o saldo da conta agora é R$${conta1.saldo}`
