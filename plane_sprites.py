import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 刷新的帧率
FRAME_PER_SEC = 60

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed = 1) -> None:
        
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
 
        self.speed = speed

    def update(self, *args) -> None:

        self.rect.y += self.speed

class BackGround(GameSprite):
    """ 游戏背景精灵 """

    def update(self, *args) -> None:
        super().update(*args)
        