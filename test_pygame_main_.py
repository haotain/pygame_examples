import pygame


pygame.init()

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

while True:
    # 可以指定时钟对象内置的频率
    clock.tick(60)

    hero_rect.y -= 1

    # 判断飞机的位置 
    if hero_rect.y <= 0:
        hero_rect.y = 700

    surface_mode.blit(bg, (0, 0))
    surface_mode.blit(hero, hero_rect)

    pygame.display.update()

pygame.quit()