import { Cliente } from "./ClasseSeparada1.js";
export class Contas
{
    static numeroConta = 0;
    corretora;
    _cliente;

    _saldo = 0;

    set cliente(novoCliente)
    {
        if(novoCliente instanceof Cliente)
        {this._cliente = novoCliente;}
    }

    get saldo()
    {
        return this._saldo
    }

    depositar(valor)
    {
        if(valor < 0) return; //return; o que eu não gostaria que acontecesse 
        {this._saldo += valor}
    }

    sacar(valor)
    {
        if(this._saldo>=valor)
        {this._saldo -= valor; return valor;}
    }

    transf(valor, Contas)
    {
        this.sacar(valor);
        Contas.depositar(valor);
    }
}
