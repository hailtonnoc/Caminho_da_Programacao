import {Cliente} from "../nodes/ClasseSeparada1.js"
import {Contas} from "../nodes/ClasseSeparada2.js"

const clienteH = new Cliente()
clienteH.nome = "Hailton";
clienteH.cpf = 45048907209;

const clienteE = new Cliente();
clienteE.nome = "Investimento Ibovespa";
clienteE.cpf = 30609984521;

const contasH = new Contas()
contasH.corretora = "NocsInvesting";
contasH.cliente = clienteH;

const contasE = new Contas();
contasE.corretora = "NocsInvesting";
contasE.cliente = clienteE;

contasH.depositar(108);
contasH.depositar(-18)
contasH.sacar(9);
//contas1.#saldo = 1 esse indica erro

console.log(contasE.saldo);

contasH.transf(18 , contasE);

console.log(contasH, contasE);
console.log(contasH.saldo)
