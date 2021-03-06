import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_MNEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT +1

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed = 1) -> None:
        
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
 
        self.speed = speed

    def update(self) -> None:

        self.rect.y += self.speed


class BackGround(GameSprite):
    """ 游戏背景精灵 """

    def __init__(self, is_alt = False) -> None:
        super().__init__('./images/background.png')

        if is_alt:
            self.rect.y = -self.rect.height


    def update(self) -> None:
        super().update()

        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self) -> None:

        # 1. 调用父类方法， 创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 2. 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
    
        # 3. 指定敌机的初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
       
    def update(self) -> None:

        # 1. 调用父类方法，保持垂直方向的飞行
        super().update()

        # 2. 判断是否飞出屏幕， 如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    
    def __del__(self):
        ...

class Hero(GameSprite):
    """ 英雄精灵 """

    def __init__(self) -> None:

        # 1. 调用父类方法， 设置image , speed
        super().__init__("./images/me1.png", 0)
        # 2. 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self) -> None:
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    
    def fire(self):
        print("发射子弹")

        for i in (0, 1, 2):

            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 设置子弹的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3. 将子弹添加到子弹组
            self.bullet_group.add(bullet)
        

class Bullet(GameSprite):
    """ 子弹精灵 """

    def __init__(self) -> None:

        # 1. 调用父类方法， 设置image , speed
        super().__init__("./images/bullet1.png", -2)
    
    def update(self):
        ...
        # 1. 调用父类方法， 设置image , speed
        super().update()

        # 2. 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()
