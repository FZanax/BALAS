"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL)


JorgePNG = pygame.image.load('assets/skins/jorge/JorgeVJ.png').convert_alpha()
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (64,64))

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Player, self).__init__()
        self.surf = JorgePNG_scaled

        self.mask = pygame.mask.from_surface(self.surf)

        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(midleft=(30, 350))
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.lives = 3
        self.is_dead = False
        self.dead_countdown = 120
        
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-4)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,4)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-6,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4,0)
        if not pressed_keys[K_UP] and not pressed_keys[K_DOWN] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT]:
            self.rect.move_ip(-2,0)

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        
        if self.is_dead:
            self.dead_countdown -= 1
        if self.dead_countdown == 0:
            self.is_dead = False
            self.dead_countdown = 120


# Definición de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definición de la clase Bullet (bala)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.speed = 10
    pass

    def update(self):
        self.rect.x = self.speed
        if self.rect.right > 1000:
            self.kill()
    pass
pass

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()