import {Cliente} from "../nodes/ClasseSeparada1.js"
import {Contas} from "../nodes/ClasseSeparada2.js"

const clienteH = new Cliente
clienteH.nome = "Hailton";
clienteH.cpf = 45048907209;

const contas1 = new Contas()
contas1.corretora = "NocsInvesting";
contas1.cliente = clienteH

contas1.depositar(108);
contas1.sacar(9);
contas1.depositar(900);
contas1.sacar(0);
//contas1.#saldo = 1 esse indica erro
contas1.depositar(-18)
contas1.sacar(3)
console.log(contas1)

//novo cliente e conta para transferencia

const clienteE = new Cliente
clienteE.nome = "Empreitada";
clienteE.cpf = 30609984521;

const contasE = new Contas
contasE.corretora = "NocsInvesting"
contasE.cliente = clienteE

contas1.transferir(99, contasE)
contasE.sacar(9)
contasE.extrato()