import pygame as PG
from pygame.locals import *
#=======================================================================#
#                           Variables globales                          #
#=======================================================================#

nRes = (1000,1000)  # -Tupla con la Resolución en x e y respectivamente.
running = True      # -Booleano para utilizar en el while principal.
Lado = 50           # -Longitud de los lados de los sprites, son de 
                    #  50 x 50.
Clock  = PG.time.Clock()    # -Utilizamos la función clock y la asignamos a
                            #  la variable para modificar los FPS.
matriz = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
#=======================================================================#
#                                 Clases                                #
#=======================================================================#

class Jugador():
    def __init__(self):     # -Caracteristicas iniciales de la clase Jugador.
        self.nT = 4         # -Variable para elegir el sprite.
        self.x = 0          # -Posición en x.
        self.y = 50         # -Posición en y.
        self.dx = 0         # -Dirección en x.
        self.dy = 0         # -Dirección en y.
        self.nV = 1         # -Velocidad.

    def Update(self,tecla,Sprites,Screen):  # La función Update realiza el
        if tecla[PG.K_RIGHT]:               # movimiento y cambio de
            self.nT = 4                     # Sprites del jugador.
            self.dx = 1 ; self.dy = 0       #  Parametros:
        if tecla[PG.K_LEFT]:                # -tecla: identifica la tecla
            self.nT = 3                     # presionada.
            self.dx = -1 ; self.dy = 0      # -Sprites:Arreglo de Sprites.
        if tecla[PG.K_UP]:                  # -Screen: Surface(Panta).
            self.nT = 5
            self.dx = 0 ; self.dy = -1
        if tecla[PG.K_DOWN]:
            self.nT = 2
            self.dx = 0 ; self.dy = 1
        self.x += self.dx * self.nV         #Actualiza la posición en x.
        self.y += self.dy * self.nV         #Actualiza la posición en y.
        Screen.blit(Sprites[self.nT],(self.x,self.y))   #Pinta el jugador.
        return

class Mapa():
    #def __init__(self):    # NO SE PORQUE SI ASIGNABA SELF.Y EN LA                
    #    self.y = 0         # FUNCION __INIT__ SE PINTA MAL EL CÓDIGO

    def Pinta(self,Screen,Res,Lado,matriz,Sprites): # 'Pinta' pinta cada
        self.y = 0  # Posición en y.                   celda de la matriz.
        for nF in range(Res[1] // Lado): # Sacamos cada fila.
            self.x = 0 #Posición en x.
            for nC in range(Res[0] // Lado): # Sacamos cada columna.
                if matriz[nF][nC] == 1:
                    self.nT = 0     #Verificamos con el valor de la matriz si
                    Screen.blit(Sprites[self.nT],(self.x,self.y))# es pared o
                if matriz[nF][nC] == 0:                          # camino.
                    self.nT = 1
                    Screen.blit(Sprites[self.nT],(self.x,self.y))
                self.x += 50
            self.y += 50
        return

#=======================================================================#
#                                Funciones                              #
#=======================================================================#

def Init_PG():
    PG.init()
    PG.mouse.set_visible(False)
    PG.display.set_caption('Laberinto - Niko Vzz')
    return PG.display.set_mode(nRes)

def Load_Image(sFile,transp = False):
    try: image = PG.image.load(sFile)
    except PG.error.message:
        raise SystemExit.message
    image = image.convert()
    if transp:
        color = image.get_at((0,0))
        image.set_colorkey(color)
    return image

def Sprt():
    lista = [
            Load_Image('Sprites\Pared.jpg'      , False),   #[0]
            Load_Image('Sprites\Camino.jpg'     , False),   #[1]
            Load_Image('Sprites\Robot_Down.png' , True ),   #[2]
            Load_Image('Sprites\Robot_Left.png' , True ),   #[3]
            Load_Image('Sprites\Robot_Right.png', True ),   #[4]
            Load_Image('Sprites\Robot_Up.png'   , True )    #[5]
            ]
    lista[2] = PG.transform.scale(lista[2],(50,50))
    lista[3] = PG.transform.scale(lista[3],(50,50))
    lista[4] = PG.transform.scale(lista[4],(50,50))
    lista[5] = PG.transform.scale(lista[5],(50,50))
    return lista

#=======================================================================#
#                       Asignación de                                   #
#                           funciones y clases                          #
#                               para su utilización                     #
#=======================================================================#

Panta = Init_PG()           # -Asignamos la surface e inicializamos pygame.
aSprt  = Sprt()             # -Asignamos el arreglo de sprites para usarlos.
aPlayer = Jugador()         # -Iniciamos y asignamos la clase jugador.
aMap = Mapa()               # -Iniciamos y asignamos  la clase aMap.

#=======================================================================#
#                           While principal                             #
#=======================================================================#
while running:                  # -running(por defecto en True).
    event = PG.event.get()      # -Obtener eventos.
    Key = PG.key.get_pressed()  # -Variable para identificación de teclas.
    for e  in event:            # -Recorremos los eventos.
        if e.type == PG.QUIT:   # -Verificamos si se presiona la x de la
            running = False     #  ventana o escape para apagar el while.
        if Key[PG.K_ESCAPE]:
            running = False
    aMap.Pinta(Panta,nRes,Lado,matriz,aSprt)  # -Utilizamos la funcion Pinta
    aPlayer.Update(Key,aSprt,Panta)           # y Update para pintar el mapa
    PG.display.flip()   #Actualizamos la      # con el robot y su movimiento.
    Clock.tick(100)     #pantalla con sus FPS.

PG.quit     # pygame off