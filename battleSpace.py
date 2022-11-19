import random
import pygame

import sys
import configuracion
from class_personajes.nave import Nave
from class_personajes.enemigo import Enemigo
from class_personajes.roca import Roca

pygame.init()

ventana = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))

pygame.display.set_icon(configuracion.iconoimagen)
pygame.display.set_caption(configuracion.nombre_ventana)
jugador_grupo = pygame.sprite.Group()
configuracion.musica_fondo.play(-1)
a = 0
b = 0


def cerrar():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def ventana_fondo():
    a = 0
    t = True
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                t = False
                break
        x_relativa = a % configuracion.fondo_ventana.get_rect().width
        ventana.blit(configuracion.fondo_ventana, (x_relativa - configuracion.fondo_ventana.get_rect().width, b))
        if x_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.fondo_ventana, (x_relativa, 0))
        a -= 1
        ventana_entrada()
        pygame.display.update()


def ventana_entrada():
    a = random.randrange(0, 255)
    b = random.randrange(0, 255)
    c = random.randrange(0, 255)
    color = (a, b, c)
    ventana.blit(configuracion.imagen_ventana, (350, 50))
    configuracion.muestra_texto(ventana, configuracion.CONSOLA, "-BATTLE SPACE-", configuracion.BLANCO, 65,
                                configuracion.ANCHO / 2, configuracion.ALTO / 2)
    configuracion.muestra_texto(ventana, configuracion.CONSOLA, "<PRESIONA ESPACIO>", color, 25,
                                configuracion.ANCHO / 2, configuracion.ALTO - 250)
    pygame.time.wait(60)

def hasPerdido():
    a = 0
    t = True
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                t = False
                break
        x_relativa = a % configuracion.fondo_ventana.get_rect().width
        ventana.blit(configuracion.fondo_ventana, (x_relativa - configuracion.fondo_ventana.get_rect().width, b))
        if x_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.fondo_ventana, (x_relativa, 0))
        textoPerdido()
        pygame.display.update()

def textoPerdido():
    a = random.randrange(0, 255)
    b = random.randrange(0, 255)
    c = random.randrange(0, 255)
    color = (a, b, c)
    ventana.blit(configuracion.imagen_ventana, (350, 50))
    configuracion.muestra_texto(ventana, configuracion.CONSOLA, "-HAS PERDIDO-", configuracion.BLANCO, 65,
                                configuracion.ANCHO / 2, configuracion.ALTO / 2)
    configuracion.muestra_texto(ventana, configuracion.CONSOLA, "<PRESIONA ESPACIO>", color, 25,
                                configuracion.ANCHO / 2, configuracion.ALTO - 250)
    pygame.time.wait(60)


def juegoInicio():
    a = 0
    j = True
    for i in range(5):
        metiorito = Roca()
        configuracion.metiorito_grupo.add(metiorito)
    for i in range(5):
        ene = Enemigo()
        configuracion.grupo_enemegios.add(ene)
    nave = Nave()
    jugador_grupo.add(nave)
    valor = 0
    while j:
        cerrar()
        # fondo en movimiento
        x_relativa = a % configuracion.fondo_ventana.get_rect().width
        ventana.blit(configuracion.fondo_ventana, (x_relativa - configuracion.fondo_ventana.get_rect().width, b))
        if x_relativa < configuracion.ANCHO:
            ventana.blit(configuracion.fondo_ventana, (x_relativa, 0))
        a -= 1
        # grupos de coliciones
        colision_jugador = pygame.sprite.spritecollide(nave, configuracion.grupo_enemegios, True,
                                                       pygame.sprite.collide_circle)
        colision = pygame.sprite.groupcollide(configuracion.grupo_enemegios, configuracion.bala_grupo, True, True,
                                              pygame.sprite.collide_circle)
        colision_metiorito = pygame.sprite.groupcollide(jugador_grupo, configuracion.metiorito_grupo, True, True,
                                                        pygame.sprite.collide_circle)
        if colision_jugador:
            nave.kill()
            j = False
            valor = 0
            nave = Nave()
            jugador_grupo.add(nave)
        if colision:
            valor += 10
            for i in range(2):
                e = Enemigo()
                configuracion.grupo_enemegios.add(e)
        if colision_metiorito:
            j = False

        # actulizacion y animacion de spritp
        configuracion.animacion_explp.update()
        jugador_grupo.update()
        configuracion.metiorito_grupo.update()
        configuracion.bala_grupo.update()
        configuracion.grupo_enemegios.update()
        configuracion.muestra_texto(ventana, configuracion.CONSOLA, str(valor).zfill(4), configuracion.BLANCO, 25, 845,
                                    15)
        jugador_grupo.draw(ventana)
        configuracion.metiorito_grupo.update()
        configuracion.animacion_explp.draw(ventana)
        configuracion.metiorito_grupo.draw(ventana)
        configuracion.grupo_enemegios.draw(ventana)
        configuracion.bala_grupo.draw(ventana)
        pygame.display.update()
    #al perder se quita de la ventana
    configuracion.metiorito_grupo.empty()
    jugador_grupo.empty()
    configuracion.grupo_enemegios.empty()
    configuracion.animacion_explp.empty()
    configuracion.bala_grupo.empty()




run = True
while run:
    configuracion.reloj.tick(configuracion.fotogramas)
    cerrar()
    ventana_fondo()
    juegoInicio()
    hasPerdido()
    pygame.display.update()
pygame.quit()
sys.exit()
