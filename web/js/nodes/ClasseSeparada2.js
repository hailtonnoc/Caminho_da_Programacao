export class Contas
{
    corretora;
    cliente;

    #saldo = 0;

    depositar(valor)
    {
        if(valor < 0) return; // o que eu não gostaria que acontecesse 
        {this.#saldo += valor}
    }

    sacar(valor)
    {
        if(valor <= this.#saldo)
        {this.#saldo -= valor}
        console.log('saldo atual '+ this.#saldo)

    }
    transferir(valor, Conta)
    {
        const valorSacado = this.sacar(valor);
        Conta.depositar(valorSacado);
    }
    extrato()
    {
        console.log(this.#saldo)
    }
}
