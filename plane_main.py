from typing import Tuple
import pygame
from pygame import event
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

        while True:
            # 1. 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)

            # 2. 事件监听
            self.__event_handler()
                
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新、 绘制精灵组
            self.____update_sprites()
            # 5. 更新显示
            pygame.display.update()
            

    def __event_handler(self):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
    
    def __check_collide(self):
        ...

    def __update_sprites(self):
        ...

    @staticmethod
    def __game_over():

        pygame.quit()
        exit()


if __name__ == '__main__':
    
    game = PlaneGame()
    game.start_game()