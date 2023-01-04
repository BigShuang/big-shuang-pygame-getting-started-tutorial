import pygame
import sys

pygame.init()
win = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()

# 新建矩形
rect1 = pygame.Rect(100, 20, 200, 60)
# 绘制矩形
pygame.draw.rect(win, "yellow", rect1, width=5)

# 绘制圆形
pygame.draw.circle(win, "blue", (100, 150), 50, width=5)

# 三个顶点的横纵坐标
points = [
    (300, 100),
    (250, 200),
    (350, 200),
]
# 用三个顶点去绘制多边形，即可得到三角形
pygame.draw.polygon(win, "green", points, width=5)

# 指定起点与终点的坐标
start = (100, 240)
end = (300, 240)
# 根据起点与终点坐标绘制线段
pygame.draw.line(win, "white", start, end, width=5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.update()