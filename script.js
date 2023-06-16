const CanvasAncho = 640
const CanvasAlto = 640
const LaberintoAncho = 20
const LaberintoAlto = 20
const PixelTam = 32


let Celdas = []
let Camino = [];
let Camino2 = [];
let Pila = []
let Inicio
let Salida
let Mario 
let Estrella
let a = 0
let b
let temp

function setup(){
  Celdas = []
  Pila = []
  Inicio = Math.round(Math.random()*LaberintoAncho)
  Salida = Math.round(Math.random()*LaberintoAncho)
  b = Inicio
  Mario = loadImage("./Mario1.png")
  Estrella = loadImage("./estrella1.png")
  const Canvas = createCanvas(CanvasAncho,CanvasAlto)
  Canvas.parent('#Canvas')
  
  for(let y=0; y<LaberintoAncho;y++){
    const Fila = []
    for(let x=0; x<LaberintoAlto;x++){
      Fila.push(new Celda(x,y))
    }
    Celdas.push(Fila)
  }
  
  const rx = Math.round(Math.random()*LaberintoAncho)
  const ry = Math.round(Math.random()*LaberintoAlto)
  
  const Primero = Celdas[ry][rx]
  Primero.visitado = true
  Pila.push(Primero)
}

function draw(){
  background("#000000")
  while(Pila.length > 0){
    let actual = Pila[Pila.length-1]
    let valido = false
    let verficados = 0
    while(!valido && verficados < 10){
      verficados++
      let posicion = Math.round(Math.random()*4)
      switch(posicion){
        //Izquierda
        case 0:
          if(actual.x > 0){
            let siguiente = Celdas[actual.y][actual.x - 1]
            if(!siguiente.visitado){
              actual.izquierda = false
              siguiente.derecha = false
              siguiente.visitado = true
              Pila.push(siguiente)
              valido = true
            }
          }
          break
          //Arriba
          case 1:
            if(actual.y > 0){
              let siguiente = Celdas[actual.y - 1][actual.x]
              if(!siguiente.visitado){
                actual.arriba = false
                siguiente.abajo = false
                siguiente.visitado = true
              Pila.push(siguiente)
              valido = true
            }
          }
          break
          //Derecha
          case 2:
            if(actual.x < (LaberintoAncho-1)){
              let siguiente = Celdas[actual.y][actual.x+1]
              if(!siguiente.visitado){
                actual.derecha = false
                siguiente.izquierda = false
                siguiente.visitado = true
                Pila.push(siguiente)
                valido = true
              }
            }
            break
            //Abajo
            case 3:
              if(actual.y < (LaberintoAlto-1)){
                let siguiente = Celdas[actual.y + 1][actual.x]
                if(!siguiente.visitado){
                  actual.abajo = false
                  siguiente.arriba = false
                  siguiente.visitado = true
                  Pila.push(siguiente)
                  valido = true
                }
              }
              break
            }
          }
    if(!valido){
      Pila.pop()
    }
  }
  for(let y=0; y<LaberintoAncho;y++){
    for(let x=0; x<LaberintoAlto;x++){
      Celdas[x][y].draw(PixelTam)
    }
  }
  Celdas[a][b].colorear(Mario,PixelTam)
  Celdas[LaberintoAlto-1][Salida].colorear(Estrella,PixelTam)
}


// Colocar cronometro y marcar la ruta que sigue mario
async function inicar(){
  DFS()
  console.log(Camino2)
  while(Camino.length){
    temp = Camino.pop()
    temp2 = Camino2.pop()
    a = temp.x
    b = temp.y
    temp2.camino = true
    await delay(300)
  }
  stopTimer()
}

function pintar(x,y){
  
}

function DFS(){
  function explora(x,y){
    if(Celdas[x][y].visitado){
      Celdas[x][y].visitado = false
      if(x==19 && y==Salida){
        console.log("Camino encontrado")
        Camino.push({ x, y });
        Camino2.push(Celdas[x][y])
        return true
      }
      if(Celdas[x][y].abajo===false){
        if (explora(x + 1, y)){
          Camino.push({ x, y });
          Camino2.push(Celdas[x][y])
          return true; // Abajo
        } 
      }
      if(Celdas[x][y].arriba===false){
        if (explora(x - 1, y)){
          Camino.push({ x, y });
          Camino2.push(Celdas[x][y]);
          return true; // Arriba
        } 
      }
      if(Celdas[x][y].derecha===false){
        if (explora(x, y + 1)){
          Camino.push({ x, y });
          Camino2.push(Celdas[x][y]);
          return true; // Derecha
        } 
      }
      if(Celdas[x][y].izquierda===false){
        if (explora(x, y - 1)){
          Camino.push({ x, y });
          Camino2.push(Celdas[x][y]);
          return true; // Izquierda
        } 
      }
    }
    return false
  }
  explora(0,Inicio)
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

var minutes = 0;
var seconds = 0;
var timer;

function addLeadingZero(value) {
  return value < 10 ? "0" + value : value;
}

function updateDisplay() {
  var display = document.getElementById("Cronometro");
  display.textContent = addLeadingZero(minutes) + ":" + addLeadingZero(seconds);
}

function startTimer() {
  timer = setInterval(function() {
    seconds++;
    if (seconds >= 60) {
      seconds = 0;
      minutes++;
      if (minutes >= 60) {
        minutes = 0;
      }
    }
    updateDisplay();
  }, 1000);
}

function stopTimer() {
  clearInterval(timer);
}
