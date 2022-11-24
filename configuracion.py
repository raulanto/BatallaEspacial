import random
import pygame
import os
# tamaños de la ventana
ANCHO = 900
ALTO = 600
# nombre ventana
nombre_ventana = "Batlle Space"
# colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Grupos de sprint
grupo_enemegios = pygame.sprite.Group()
bala_grupo = pygame.sprite.Group()
animacion_explp = pygame.sprite.Group()
metiorito_grupo = pygame.sprite.Group()
# fotogramas
fotogramas = 60
reloj = pygame.time.Clock()
#haciedno rutas de las imagenes
carpeta_juego=os.path.dirname(__file__)
carpeta_iconos=os.path.join(carpeta_juego,"iconos")
carpeta_fondo=os.path.join(carpeta_juego,"fondos")
carpeta_sonido=os.path.join(carpeta_juego,"sonidos")
capeta_explo=os.path.join(carpeta_juego,"explocion")
carpeta_enemigos=os.path.join(carpeta_juego,"clutu1")
carpeta_enemigos2=os.path.join(carpeta_juego,"izquierda")
carpeta_personajes=os.path.join(carpeta_juego,"personajes")
# icono imagen
i = random.randrange(20, 26)
iconoimagen = pygame.image.load(os.path.join(carpeta_iconos,f"Imagen{i}.png"))
imagen_ventana = pygame.transform.scale(iconoimagen, (200, 200))

# fondo imagen
i = random.randrange(2)+1
fondo_ventana = pygame.image.load(os.path.join(carpeta_fondo,f"fondo_extendido{i}.png"))
fondo_ventana = pygame.transform.scale(fondo_ventana, (2000, ALTO))

# tipografias
CONSOLA = pygame.font.match_font("04B_30")

# funciones
def muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(fuente, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie, rectangulo)

#Musica
pygame.mixer.init()
musica_fondo=pygame.mixer.Sound(os.path.join(carpeta_sonido,"fondomusic.mp3"))
musica_fondo.set_volume(0.1)
sonido_disparo=pygame.mixer.Sound(os.path.join(carpeta_sonido,"laser.wav"))