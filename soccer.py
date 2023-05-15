import pygame
import sys
import math
import random
JugadorT1 = ['J1P1.png']
JugadorT2 = ['J2P1.png']
Ball_speed_x = 1
Ball_speed_y = 1

goles_Blancos = 0
goles_Azules = 0

class Player(pygame.sprite.Sprite):

    def __init__(self, image_path, x, y,id):
        super().__init__()
        self.id = id
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self,Ball):
        global goles_Blancos 
        global goles_Azules 
        global Ball_speed_x,Ball_speed_y
        if self.id == 0:       
            if((self.rect.x >= 50 and self.rect.x <= 832)and(self.rect.y >= 125 and self.rect.y <= 610)):
                self.rect.x += Ball_speed_x
                self.rect.y += Ball_speed_y
                
                if self.rect.x == 50 or self.rect.x == 832:
                    Ball_speed_x = -Ball_speed_x
                    if self.rect.y >= 300 and self.rect.y <= 390:
                        if self.rect.x == 50:
                            goles_Azules += 1
                            self.rect.x = 442
                            self.rect.y = 367

                        if self.rect.x == 832:
                            goles_Blancos += 1
                            self.rect.x = 442
                            self.rect.y = 367
                               
                if self.rect.y == 125 or self.rect.y == 610:
                    Ball_speed_y = -Ball_speed_y
                    
                
        else:
#------------Equipo Blanco
            #Portero
            if self.id == 1 and self.rect.x<80:
                limites(self,50,80,300,390)
            #Defensas
            if self.id == 2 and self.rect.x>95 and self.rect.x<427 and self.rect.y > 130 and self.rect.y < 570:
                limites(self, 95,427,130,570)     
            if self.id == 3 and self.rect.x>95 and self.rect.x<427 and self.rect.y > 130 and self.rect.y < 570:
                limites(self, 95,427,130,570)
            if self.id == 4 and self.rect.x>95 and self.rect.x<427 and self.rect.y > 130 and self.rect.y < 570:
                limites(self, 95,427,130,570)
            #Delanteros
            if self.id == 5 and self.rect.x>369 and self.rect.x<785 and self.rect.y > 130 and self.rect.y < 570:
                if self.rect.x<450:
                     self.rect.x += 1
                else:
                    limites(self,369,785,130,570)
            if self.id == 6 and self.rect.x>369 and self.rect.x<785 and self.rect.y > 130 and self.rect.y < 570:
                if self.rect.x<450:
                     self.rect.x += 1
                else:
                    limites(self,369,785,130,570)
            if self.id == 7 and self.rect.x>369 and self.rect.x<785 and self.rect.y > 130 and self.rect.y < 570:
                if self.rect.x<450:
                     self.rect.x += 1
                else:
                    limites(self,369,785,130,570)
#------------Equipo Azules
            #Portero
            if self.id == 8:#and self.rect.x>805:
                limites(self,800,840,300,390)
            #Defensas
            if self.id == 9 and self.rect.x>450 and self.rect.x<785 and self.rect.y > 130 and self.rect.y < 570:
                limites(self,450,785,130,570)
            if self.id == 10 and self.rect.x>450 and self.rect.x<785 and self.rect.y > 130 and self.rect.y < 570:
                limites(self,450,785,130,570)
            if self.id == 11 and self.rect.x>450 and self.rect.x<785 and self.rect.y > 130 and self.rect.y < 570:
                limites(self,450,785,130,570)
            #Delanteros
            if self.id == 12 and self.rect.x>95 and self.rect.x<516 and self.rect.y > 130 and self.rect.y < 570:
                if self.rect.x >435:
                     self.rect.x -= 1
                else:
                     limites(self,95,430,130,570)
            if self.id == 13 and self.rect.x>60 and self.rect.x<516 and self.rect.y > 130 and self.rect.y < 570:
                if self.rect.x >435:
                     self.rect.x -= 1
                else:
                     limites(self,95,430,130,570)
            if self.id == 14 and self.rect.x>60 and self.rect.x<516 and self.rect.y > 130 and self.rect.y < 570:
                if self.rect.x >435:
                     self.rect.x -= 1
                else:
                     limites(self,95,430,130,570)
            if self.rect.colliderect(Ball.rect):
                Ball_speed_x = -Ball_speed_x
        pass

def limites(self,x1,x2,y1,y2):
    pixeles = random.randrange(1, 5)
    #pixeles = 3
    if self.rect.x <= (x1+pixeles):
                    self.rect.x += pixeles
    if self.rect.x >= (x2-pixeles):
                    self.rect.x -= pixeles
    if self.rect.y <= (y1+pixeles):
                    self.rect.y += pixeles
    if self.rect.y >= (y2-pixeles):
                    self.rect.y -= pixeles
    else:    
        if random.randint(0,1)==0: #0 arriba, 1 abajo
             self.rect.y -= pixeles
        else:
            self.rect.y += pixeles
        if random.randint(0,1)==0: #0 derecha, 1 izquierda
            self.rect.x -= pixeles
        else:
            self.rect.x += pixeles

def dibujar_boton(texto,Rect,ventana):
    if Rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(ventana,COLOR_BOTON_HOVER,Rect,border_radius=10)
    else:
        pygame.draw.rect(ventana,COLOR_BOTON,Rect,border_radius=10)
    texto_renderizado = pygame.font.SysFont(None, 36).render(texto, True, (0,0,0))
    ventana.blit(texto_renderizado, (Rect.x + Rect.width / 2 - texto_renderizado.get_width() / 2, Rect.y + Rect.height / 2 - texto_renderizado.get_height() / 2))


def Timer():
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    minutos =int((tiempo_transcurrido / 1000)/60)
    segundos = int((tiempo_transcurrido / 1000)%60)
    return f"{minutos:02d}:{segundos:02d}"
# Inicializar Pygame
pygame.init()

# Configurar la ventana
ventana_ancho = 900
ventana_alto = 702
ventana_titulo = "Soccer"
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption(ventana_titulo)
icono = pygame.image.load("icono.png")  # Reemplaza "icono.png" con la ruta a tu archivo de ícono
pygame.display.set_icon(icono)

fondo = pygame.image.load("cancha.png").convert()
fondo = pygame.transform.scale(fondo, (ventana_ancho, 512))
marcador = pygame.image.load("marcador.png").convert()
marcador = pygame.transform.scale(marcador, (600, 120))

tiempo_inicial = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos

COLOR_BOTON = (226,207,212)
COLOR_BOTON_HOVER = (162,112,125)
START = pygame.Rect(10, 642, 100, 50)
RESET = pygame.Rect(120, 642, 100, 50)
Timer_Enable = False
minutos = 0
Start_Button_Enable = True
Reset_Button_Enable = False

# Creacion Jugadores Equipo Blanco
JugadorB1 = Player(JugadorT1[0],60,350,1)
JugadorB2 = Player(JugadorT1[0],220,350,2)
JugadorB3 = Player(JugadorT1[0],220,180,3)
JugadorB4 = Player(JugadorT1[0],220,520,4)
JugadorB5 = Player(JugadorT1[0],400,350,5)
JugadorB6 = Player(JugadorT1[0],400,180,6)
JugadorB7 = Player(JugadorT1[0],400,520,7)
# Creacion Jugadores Equipo Azul
JugadorA1 = Player(JugadorT2[0],825,350,8)
JugadorA2 = Player(JugadorT2[0],665,350,9)
JugadorA3 = Player(JugadorT2[0],665,180,10)
JugadorA4 = Player(JugadorT2[0],665,520,11)
JugadorA5 = Player(JugadorT2[0],515,350,12)
JugadorA6 = Player(JugadorT2[0],515,180,13)
JugadorA7 = Player(JugadorT2[0],515,520,14)

Balon = Player("balon.png",442,367,0)

TodosJugadores = pygame.sprite.Group()
TodosJugadores.add(JugadorB1,JugadorB2,JugadorB3,JugadorB4,JugadorB5,JugadorB6,JugadorB7,JugadorA1,JugadorA2,JugadorA3,JugadorA4,JugadorA5,JugadorA6,JugadorA7,Balon)

while True:
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button==1:
            if START.collidepoint(pygame.mouse.get_pos()) and Start_Button_Enable:
                tiempo_inicial = pygame.time.get_ticks()
                Timer_Enable = True
                Start_Button_Enable = False
                Reset_Button_Enable = True
                #TodosJugadores.update(Balon) #
                #TodosJugadores.draw(ventana) #
            if RESET.collidepoint(pygame.mouse.get_pos()) and Reset_Button_Enable:
                Timer_Enable = False
                minutos = 0
                Start_Button_Enable = True
                Reset_Button_Enable = False
                #TodosJugadores.update(Balon) #
                #TodosJugadores.draw(ventana) #


    # Limpiar la ventana
    ventana.fill((99,2,36,255))
    ventana.blit(fondo, (0, 120))
    ventana.blit(marcador, (150, 0))
    dibujar_boton("START", START, ventana)
    dibujar_boton("RESET", RESET, ventana)


    if minutos >= 1:
        texto = "10:00"
    elif Timer_Enable:
        texto = Timer()
    else:
        texto = "00:00"

    texto_renderizado = pygame.font.SysFont(None, 36).render(texto, True, (255,255,255))
    Name_Team1 = pygame.font.SysFont(None, 42).render(f"Blancos  {goles_Blancos}", True, (255,255,255))
    Name_Team2 = pygame.font.SysFont(None, 42).render(f"{goles_Azules}  Azules", True, (255,255,255))
    ventana.blit(texto_renderizado, (422,12))
    ventana.blit(Name_Team1, (185,52))
    ventana.blit(Name_Team2, (565,52))

    if Start_Button_Enable==False:
        TodosJugadores.update(Balon)
        TodosJugadores.draw(ventana)

    if Reset_Button_Enable==False:
        # Creacion Jugadores Equipo Blanco
        JugadorB1 = Player(JugadorT1[0],60,350,1)
        JugadorB2 = Player(JugadorT1[0],220,350,2)
        JugadorB3 = Player(JugadorT1[0],220,180,3)
        JugadorB4 = Player(JugadorT1[0],220,520,4)
        JugadorB5 = Player(JugadorT1[0],400,350,5)
        JugadorB6 = Player(JugadorT1[0],400,180,6)
        JugadorB7 = Player(JugadorT1[0],400,520,7)
        # Creacion Jugadores Equipo Azul
        JugadorA1 = Player(JugadorT2[0],825,350,8)
        JugadorA2 = Player(JugadorT2[0],665,350,9)
        JugadorA3 = Player(JugadorT2[0],665,180,10)
        JugadorA4 = Player(JugadorT2[0],665,520,11)
        JugadorA5 = Player(JugadorT2[0],515,350,12)
        JugadorA6 = Player(JugadorT2[0],515,180,13)
        JugadorA7 = Player(JugadorT2[0],515,520,14)
        Balon = Player("balon.png",442,367,0)
        TodosJugadores = pygame.sprite.Group()
        TodosJugadores.add(JugadorB1,JugadorB2,JugadorB3,JugadorB4,JugadorB5,JugadorB6,JugadorB7,JugadorA1,JugadorA2,JugadorA3,JugadorA4,JugadorA5,JugadorA6,JugadorA7,Balon)
        minutos = 0
        goles_Azules = 0
        goles_Blancos = 0
         
    # pygame.time.wait(5)

    pygame.display.flip()
        