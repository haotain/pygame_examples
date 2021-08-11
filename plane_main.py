import pygame
from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""



    def __init__(self) -> None:
        super().__init__()

        # 1. 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size )
        # 2. 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组创建
        self.__create_sprites()

        ...
    
    def __create_sprites(self) -> None:
        ...

    def start_game(self):

        ...


if __name__ == '__main__':
    
    game = PlaneGame()
    game.start_game()