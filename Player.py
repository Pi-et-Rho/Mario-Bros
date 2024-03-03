import pygame
from Settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(r"Sprites\mario.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = SPEED
        self.jump_power = JUMP_POWER
        self.vy = 0
        self.on_ground = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vy = self.jump_power
            self.on_ground = False

    def update(self):
        self.get_input()

        if not self.on_ground:
            self.vy += GRAVITY
            self.rect.y += self.vy

            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
                self.on_ground = True
                self.vy = 0
        self.rect.x = (max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width)))