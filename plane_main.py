import pygame
from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self) -> None:
        super().__init__()

        pygame.init()

        # 1. 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size )
        # 2. 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组创建
        self.__create_sprites()
        # 设置定时器事件
        pygame.time.set_timer(CREATE_MNEMY_EVENT, 1000)

        # 设置发射子弹事件
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
    
    def __create_sprites(self) -> None:

        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        while True:
            # 1. 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)

            # 2. 事件监听
            self.__event_handler()
                
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新、 绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()
            

    def __event_handler(self):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over() 
            elif event.type == CREATE_MNEMY_EVENT: 
                ememy = Enemy()
                self.enemy_group.add(ememy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右")

        # 键盘控制英雄 左右移动    
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT]):
            self.hero.speed = 2
        elif (keys[pygame.K_LEFT]):
            self.hero.speed = -2
        else:
            self.hero.speed = 0
    def __check_collide(self):
        
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)


    @staticmethod
    def __game_over():

        pygame.quit()
        exit()


if __name__ == '__main__':
    
    game = PlaneGame()
    game.start_game()