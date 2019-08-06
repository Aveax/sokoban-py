import sys
import pygame
from selectmap import SelectMap
from sok import Sok
from map import Map
from game import Game


class LetsPlay:

    select_map = None
    game = None

    def __init__(self):
        self.create_select_map()

    def create_select_map(self):
        self.game = None
        self.select_map = SelectMap()
        pygame.display.update()

    def start_game(self, level):
        self.select_map = None
        map_obj = Map(level)
        sok = Sok(map_obj)
        sok.draw()
        self.game = Game(sok, map_obj)


pygame.init()
pygame.display.set_caption('Sokoban')
pygame.display.set_mode((450, 450))
pygame.display.update()
play = LetsPlay()

while True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and play.select_map is not None:
            pos = pygame.mouse.get_pos()
            temp = play.select_map.check_if_clicked(pos)
            if temp is not False:
                play.start_game(temp)
        elif event.type == pygame.KEYDOWN and play.game is not None:
            if play.game.check_win() is False:
                if event.key == pygame.K_LEFT:
                    play.game.move_left()
                    print(event.key)
                elif event.key == pygame.K_RIGHT:
                    play.game.move_right()
                elif event.key == pygame.K_UP:
                    play.game.move_up()
                elif event.key == pygame.K_DOWN:
                    play.game.move_down()
                elif event.key == pygame.K_r:
                    play.game.restart_level()
                elif event.key is pygame.K_ESCAPE or event.key is pygame.K_q:
                    play.create_select_map()
            elif event.key is pygame.K_ESCAPE or event.key is pygame.K_q:
                play.create_select_map()
        elif event.type == pygame.KEYDOWN and play.game is None:
            if event.key is pygame.K_ESCAPE or event.key is pygame.K_q:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
