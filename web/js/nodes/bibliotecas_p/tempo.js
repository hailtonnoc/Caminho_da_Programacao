const datas = new Date
const hora = datas.getHours()
const diaSemana = datas.getDay()
const diaMes = datas.getDate()
const gMes = datas.getMonth()

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


const localdiames = document.querySelector('div#diames')
localdiames.innerHTML = `Hoje é dia <strong style = "font-size: 1.81em; color: white;" >${diaMes}</strong>`
const diarest = mes[1] - diaMes
const localdiarest = document.querySelector('div#diarest')
localdiarest.innerHTML = `Faltam <strong style ="font-size:1.54em; color: red;">${diarest}</strong> para terminar o mês.`

const localhora = document.querySelector('div#horaspercen')

const dormiu = 6
const rhora = hora - dormiu
const hdisponivel = 18
const mdisponivel = fragsm*hdisponivel
const mpassado = (rhora*fragsm) + datas.getMinutes()


const consumo = ((mpassado/mdisponivel)*100)

localhora.innerHTML = 
`<div class="horascontrol">
        São <strong class="conthoras">${hora}</strong>horas e passaram aproximadamente <strong class="conthoras">${consumo.toFixed(2)}%</strong> do dia ativo. Restam <small style="font-size:1.27em; color: red;">${(100-consumo).toFixed(2)}%</small>
</div>`