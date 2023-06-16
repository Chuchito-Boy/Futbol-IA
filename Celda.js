class Celda {
    constructor(x,y){
        this.x = x
        this.y = y
        this.visitado = false
        this.izquierda = true
        this.derecha = true
        this.arriba = true
        this.abajo = true
        this.camino = false
    }

    draw(PixelTam){
        let x = this.x * PixelTam
        let y = this.y * PixelTam
        noStroke()
        if(this.visitado)
            fill("#40A437")
        else
            fill("#40A437")
        if(this.camino)
            fill("#FF0000")
        rect(x,y,PixelTam,PixelTam)
        stroke(0)
        strokeWeight(2)
        noFill()
        if(this.izquierda)
            line(x,y,x,y+PixelTam)
        if(this.arriba)
            line(x,y,x + PixelTam,y)
        if(this.derecha)
            line(x+PixelTam,y,x+PixelTam,y+PixelTam)
        if(this.abajo)
            line(x,y+PixelTam,x+PixelTam,y+PixelTam)  
    }
    colorear(img,PixelTam){
        let x = this.x * PixelTam
        let y = this.y * PixelTam
        image(img,x,y)
    }
}