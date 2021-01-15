        var localdiames = document.querySelector('div#diames')
        var tempo = new Date
        var diames = tempo.getDate()
        localdiames.innerHTML = `Hoje é dia <strong style = "font-size: 1.81em; color: white;" >${diames}</strong>`
        var diarest =31 - diames
        var localdiarest = document.querySelector('div#diarest')
        localdiarest.innerHTML = `Faltam <strong style ="font-size:1.54em; color: red;">${diarest}</strong> para terminar o mês.`
