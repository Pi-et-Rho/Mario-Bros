import pygame
from Settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.image = pygame.image.load(r"Sprites\mario.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.jump_speed = 10
        self.gravity = 0.5
        self.is_jumping = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = 10  # Réinitialiser la vitesse de saut au début du saut

        if self.is_jumping:
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.jump_speed < 0:  # Si le personnage atteint le sommet du saut
                self.is_jumping = False  # Arrêter le saut et commencer la chute
                self.gravity = -0.5  # Inverser la gravité pour la phase de chute

        else:  # Si le personnage est en train de tomber
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.rect.y >= SCREEN_HEIGHT * 2 / 3:
                self.rect.y = SCREEN_HEIGHT * 2 / 3
                self.jump_speed = 0
                self.gravity = 0.5 

    def update(self):
        self.get_input()