import os

import pygame
import random
import configuracion
import os

class Roca(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image = pygame.image.load(os.path.join(configuracion.carpeta_personajes,"roca.tif")).convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.image.set_colorkey(configuracion.NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 32
        self.rect.x = random.randrange(configuracion.ANCHO - self.rect.width)
        self.rect.y = random.randrange(self.rect.width)
        self.velocidad_y = 1

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > configuracion.ALTO:
            self.rect.x = random.randrange(configuracion.ANCHO - self.rect.width)
            self.rect.y = self.rect.width
            self.velocidad_y = 1

class Detonacion(pygame.sprite.Sprite):
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