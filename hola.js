let BotonGenerar = document.getElementById("BotonGenerar");
let BotonInicar = document.getElementById("BotonIniciar")

BotonGenerar.addEventListener('click',function(){
    location.reload()
})

BotonInicar.addEventListener('click',function(){
    inicar()
    startTimer()
})