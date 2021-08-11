import pygame
from pygame import surface
from plane_sprites import *

pygame.init()
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 创建游戏的窗口
surface_mode = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2 blit 绘制图像
surface_mode.blit(bg, (0,0))
# 3 加载到窗口
# pygame.display.update()

# 绘制飞机
hero = pygame.image.load("./images/me1.png")

surface_mode.blit(hero, (200, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 初始化飞机位置
hero_rect = pygame.Rect(200, 500, 102, 126)

# 创建敌机的精灵
ememy = GameSprite("./images/enemy1.png")
ememy1 = GameSprite("./images/enemy1.png", 2)
# 创建敌机精灵组
ememy_group = pygame.sprite.Group(ememy, ememy1)


while True:
    # 可以指定时钟对象内置的频率
    clock.tick(60)

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    hero_rect.y -= 1

    # 判断飞机的位置 
    if hero_rect.y <= 0:
        hero_rect.y = 700

    surface_mode.blit(bg, (0, 0))
    surface_mode.blit(hero, hero_rect)

    # 让组中的所以精灵更新位置
    ememy_group.update()
    # 在 screen 上绘制所有精灵
    ememy_group.draw(surface_mode)

    pygame.display.update()

pygame.quit()