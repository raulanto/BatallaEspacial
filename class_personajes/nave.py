import pygame
import configuracion
import os
NIVEL_SUELO = 0


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load(os.path.join(configuracion.carpeta_personajes,"Imagen1.tif")).convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.image.set_colorkey(configuracion.NEGRO)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # darle forma de circulo
        self.radius = 30
        # velocidad de la bala
        self.cadencia = 750
        # Centra el rectángulo (sprite)
        self.rect.centerx = configuracion.ANCHO / 2
        self.rect.centery = configuracion.ALTO - 30
        # velocidad del personaje inicial
        self.velocidad_x = 0

        self.velocidad_inicial = 0
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self):
        # velocidad predeterminada cada vuelta  del blcle si no pulsas nada
        self.velocidad_x = 0

        # mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 10

        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -10

        if teclas[pygame.K_SPACE]:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia:
                self.disparo()
                self.disparo2()
                self.disparo3()
                self.ultimo_disparo = ahora
        if teclas[pygame.K_UP]:
            self.velocidad_inicial = -10
            self.actualizar_salto()
        else:
            self.actualizar_salto()

        # actuliza la posicion del personaje
        self.rect.x += self.velocidad_x
        # margen superior izquierdo
        if self.rect.left < 0:
            self.rect.left = 0

        # Limita el margen derecho
        if self.rect.right > configuracion.ANCHO:
            self.rect.right = configuracion.ANCHO

        # Limita el margen inferior
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

        # Limita el margen superior
        if self.rect.top < 0:
            self.rect.top = 0

    def disparo(self):
        from class_personajes.disparo import Disparo
        bala = Disparo(self.rect.centerx, self.rect.top)
        configuracion.bala_grupo.add(bala)
        configuracion.sonido_disparo.play()

    def disparo2(self):
        from class_personajes.disparo import Disparo
        bala2 = Disparo(self.rect.centerx - 23, self.rect.top)
        configuracion.bala_grupo.add(bala2)
        configuracion.sonido_disparo.play()

    def disparo3(self):
        from class_personajes.disparo import Disparo
        bala3 = Disparo(self.rect.centerx + 23, self.rect.top)
        configuracion.bala_grupo.add(bala3)
        configuracion.sonido_disparo.play()

    def kill(self):
        super(Nave, self).kill()
        explo = Explosion(self.rect.centerx, self.rect.centery)
        configuracion.animacion_explp.add(explo)

    def actualizar_salto(self):
        # si está saltando actualiza su posición
        self.rect.y += self.velocidad_inicial
        self.velocidad_inicial += 0.5


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
