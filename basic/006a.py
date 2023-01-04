import pygame
import sys

WIDTH, HEIGHT = 300, 300

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

lines = [
    "竹枝词",
    "唐·刘禹锡",
    "",
    "山桃红花满上头",
    "蜀江春水拍山流",
    "花红易衰似郎意",
    "水流无限似侬愁"
]

font = pygame.font.SysFont("kaiti", 24)
sy = 40
i = 0

win.fill("lavender")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 判断当前事件是否为点击右上角退出键
            pygame.quit()
            sys.exit()  # 需要提前 import sys

        if event.type == pygame.MOUSEBUTTONDOWN:
            if i < len(lines):
                line = lines[i]  # 通过索引取到对用的行
                text = font.render(line, True, "red")
                text_width, text_height = text.get_size()
                yi = sy + i * 30  # 计算对应的纵坐标，索引即行号，30是行高
                xi = WIDTH // 2 - text_width // 2
                win.blit(text, (xi, yi))
                i += 1

    clock.tick(60)
    pygame.display.update()