import pygame
from Settings import *

class Map:
    def __init__(self):
        # Charger l'image pour le sol
        self.texture_ground = pygame.image.load(r"Sprites\ground.png").convert_alpha()
        self.texture_ground = pygame.transform.scale(self.texture_ground, (TEXTURE_WIDTH, TEXTURE_HEIGHT))
        # Charger l'image pour les blocs
        self.texture_blocks = pygame.image.load(r"Sprites\blocks.png").convert_alpha()
        self.texture_blocks = pygame.transform.scale(self.texture_blocks, (BLOCK_SIZE, BLOCK_SIZE))
        # Nombre de tuiles nécessaires pour remplir l'écran
        self.num_tiles = SCREEN_WIDTH // TEXTURE_WIDTH
        # Liste des blocs
        self.blocks = []
        # Ajouter des blocs à la carte
        self.add_blocks()
        # Décalage horizontal de la vue de la carte
        self.x_offset = 0

    def update(self, player):
        if player.rect.right > SCREEN_WIDTH * 0.98:
            self.x_offset += player.speed
        if player.rect.left < 1:
            self.x_offset -= player.speed

    def add_blocks(self):
        self.blocks.append((60, SCREEN_HEIGHT - 100))
        self.blocks.append((220, SCREEN_HEIGHT - 100))
        self.blocks.append((580, SCREEN_HEIGHT - 100))
        self.blocks.append((970, SCREEN_HEIGHT - 100))

    def draw(self, screen):
        for i in range(self.num_tiles + 1):
            screen.blit(self.texture_ground, (i * TEXTURE_WIDTH - self.x_offset % TEXTURE_WIDTH, SCREEN_HEIGHT - TEXTURE_HEIGHT))

        for block in self.blocks:
            screen.blit(self.texture_blocks, (block[0] - self.x_offset, block[1]))
    