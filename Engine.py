import pygame, sys
from Settings import *
from Player import *
from Map import *

class Game:
    def __init__(self):
        #Player
        player_sprite = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT))
        self.player = pygame.sprite.GroupSingle(player_sprite)
        #Health/Score

        #Map
        self.game_map = Map()
        #Ennemies

        #Extra


    def run(self):
        self.player.update()
        self.game_map.update(self.player.sprite)
        screen.fill(SCREEN_COLOR)
        self.game_map.draw(screen)
        self.player.draw(screen)


if __name__ == "__main__":

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run()

        pygame.display.flip()
        clock.tick(CLOCK_TICK)