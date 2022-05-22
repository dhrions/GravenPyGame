# Ce code provient est tiré de cette vidéo YT : https://www.youtube.com/watch?v=ooITOxbYVTo&t=304s

# Import des modules
import pygame
import pytmx
import pyscroll

from game import Game

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()