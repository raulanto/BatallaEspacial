import pygame
import random
import os

import configuracion
from configuracion import NEGRO,ANCHO,animacion_explp

tamano_imagen = (64, 64)


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # elegir una imagen al ramdom
        self.df = random.randrange(7) + 1
        self.image = pygame.image.load(os.path.join(configuracion.carpeta_enemigos,f"Imagen{self.df}.tif")).convert()
        self.image = pygame.transform.scale(self.image, tamano_imagen)
        self.image.set_colorkey(NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 32
        # Centra el rectángulo (sprite)
        self.rect.centerx = random.randrange(10, 600)
        self.rect.centery = random.randrange(1, 50)
        # velocidad del personaje inicial ramdom
        self.velocidad_aleatoria_x = random.randrange(1, 10)
        self.velocidad_aleatoria_y = random.randrange(1, 10)

    def update(self):
        self.rect.x += self.velocidad_aleatoria_x
        self.rect.y += self.velocidad_aleatoria_y
        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_aleatoria_x += 1
            self.image = pygame.image.load(os.path.join(configuracion.carpeta_enemigos,f"Imagen{self.df}.tif")).convert()
            self.image = pygame.transform.scale(self.image, tamano_imagen)
            self.image.set_colorkey(NEGRO)

        # Limita el margen derecho
        if self.rect.right >ANCHO:
            self.velocidad_aleatoria_x -= 1
            self.image = pygame.image.load(os.path.join(configuracion.carpeta_enemigos2,f"Imagen{self.df}.tif")).convert()
            self.image = pygame.transform.scale(self.image, tamano_imagen)
            self.image.set_colorkey(NEGRO)

        # Limita el margen inferior
        if self.rect.bottom >= 600:
            self.velocidad_aleatoria_y -= 1

        # Limita el margen superior
        if self.rect.top < 0:
            self.velocidad_aleatoria_y += 1

    def kill(self):
        super(Enemigo, self).kill()
        explo = Explosion(self.rect.centerx, self.rect.centery)
        animacion_explp.add(explo)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(4, 10):
            img = pygame.image.load(os.path.join(configuracion.capeta_explo,f"Imagen{num}.tif"))
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 4
        # update explosion animation
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        # if the animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()
