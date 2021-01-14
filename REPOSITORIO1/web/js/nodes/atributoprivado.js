class contas
{
    corretora;
    #saldo = 0;

    depositar(valor)
    {
        if(valor > 0)
        {this.#saldo += valor}
    }

    sacar(valor)
    {
        if(valor <= this.#saldo)
        {this.#saldo -= valor}
        {console.log(contas1.#saldo)}

    }
}

const contas1 = new contas()
contas1.corretora = "NocsInvesting";

contas1.depositar(108);
contas1.sacar(9);
contas1.depositar(900);
contas1.sacar(0);
contas1.#saldo = 1
contas1.sacar(0);