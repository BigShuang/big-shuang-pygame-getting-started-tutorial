import pygame
import sys

pygame.init()
win = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()

# 画矩形
left, top, width, height = 100, 50, 200, 100
rect1 = pygame.Rect(left, top, width, height)
# 建立字体
font = pygame.font.SysFont(None, 24)
# 建立显示对应的文本字符串
info = "out"

while True:
    # 刷新界面（重置背景）
    win.fill("black")
    pygame.draw.rect(win, "yellow", rect1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 判断事件类型
        if event.type == pygame.MOUSEMOTION:
            px, py = event.pos
            # 判断坐标是否在矩形中
            if left <= px <= left + width and top <= py <= top + height:
                info = "in"
            else:
                info = "out"

    # 绘制文本与矩形
    text = font.render(info, True, "green")
    win.blit(text, (150, 200))

    clock.tick(60)
    pygame.display.update()