
var datas = new Date
var hora = datas.getHours()
var diaSemana = datas.getDay()
var diaMes = datas.getDate()
var gMes = datas.getMonth()

//fragmento segundos ou minutos 
const fragsm = 60
//horas do dia 
const fragdia = 24

//dia semana
switch(diaSemana)
{
    case 0:
        var dias = "Domingo"
    case 1:
        var dias = "Segunda"
        break;
    case 2:
        var dias = "Terça"
        break;
    case 3:
        var dias = "Quarta"
        break;
    case 4:
        var dias = "Quinta"
        break;
    case 5:
        var dias ="Sextou"
        break;
    case 6:
        var dias  = "Sabado"
        break;
        
        default:
        document.write(`o dia ${dias} não é um dia valido. Ou seu programa esta incompleto.`)
        break;
}

//Mes
switch(gMes)
{
    case 0:
        var mes = ["Janeiro", 31]
        break;
    case 1:
        var mes = ["Fevereiro", 28]
        break;
    case 2:
        var mes = ["Março", 31]
        break;
    case 3:
        var mes = ["Abril", 30]
        break;
    case 4:
        var mes = ["Maio", 31]
        break;
    case 5:
        var mes = ["Junho", 30]
        break;
    case 6:
        var mes = ["Julho", 31]
        break;
    case 7:
        var mes = ["Agosto", 31]
        break;
    case 8:
        var mes = ["Setembro", 30]
        break;
    case 9:
        var mes = ["Outubro", 31]
        break;
    case 10:
        var mes = ["Novembro", 30]
        break;
    case 11:
        var mes = ["Dezembro", 31]
        break;
}

console.log(mes)
