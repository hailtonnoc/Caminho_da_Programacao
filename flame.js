        const localdiames = document.querySelector('div#diames')
        const tempo = new Date
        const diames = tempo.getDate()
        localdiames.innerHTML = `Hoje é dia <strong style = "font-size: 1.81em; color: white;" >${diames}</strong>`
        const diarest =28 - diames
        const localdiarest = document.querySelector('div#diarest')
        localdiarest.innerHTML = `Faltam <strong style ="font-size:1.54em; color: red;">${diarest}</strong> para terminar o mês.`

        const horas = tempo.getHours()
        const localhoras = document.querySelector('div#horaspercen')
        
        const dormiu = 6
        const rhora = horas - dormiu
        const hdisponivel = 18
        const mdisponivel = 60*hdisponivel
        const mpassado = (rhora*60) + tempo.getMinutes()


        const consumo = ((mpassado/mdisponivel)*100)
        
        localhoras.innerHTML = 
        `<div class="horascontrol">
                São <strong class="conthoras">${horas}</strong>horas e passaram aproximadamente <strong class="conthoras">${consumo.toFixed(2)}%</strong> do dia ativo. Restam <small style="font-size:1.27em; color: red;">${(100-consumo).toFixed(2)}%</small>
        </div>`


