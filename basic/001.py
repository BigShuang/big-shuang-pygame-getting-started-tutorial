import pygame

pygame.init() # pygame初始化，必须有，且必须在开头

# 创建主窗体, (400,200)会将窗体长设置为400，高设置为200
win = pygame.display.set_mode((400,200))

# 用于控制循环刷新频率的对象
clock = pygame.time.Clock()

while True:
    clock.tick(60)  # 控制循环刷新频率,每秒刷新60次
    pygame.display.update()


