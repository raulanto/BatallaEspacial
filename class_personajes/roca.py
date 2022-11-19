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
