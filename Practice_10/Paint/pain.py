import pygame, sys

pygame.init()
SW, SH, TH = 800, 600, 50
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)

PALETTE = [
    (0,0,0),(255,255,255),(220,50,50),(50,200,50),
    (40,80,220),(255,220,0),(255,140,0),(140,0,180),
]
TOOLS = [("pencil",8),("eraser",90),("rect",172),("circle",254)]

tool  = "pencil"
color = (0, 0, 0)
brush = 4
canvas = pygame.Surface((SW, SH - TH)); canvas.fill((255,255,255))
drawing = False
sx = sy = 0

while True:
    clock.tick(60)
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type == pygame.MOUSEWHEEL:
            brush = max(1, min(50, brush + event.y))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if my < TH:
                for t, bx in TOOLS:
                    if bx <= mx <= bx+64 and 8 <= my <= 42: tool = t
                for i, c in enumerate(PALETTE):
                    x = 340 + i*33
                    if x <= mx <= x+28 and 10 <= my <= 38: color = c
            else:
                drawing = True; sx = mx; sy = my - TH
                if tool == "pencil": pygame.draw.circle(canvas, color, (sx,sy), brush//2)
                if tool == "eraser": pygame.draw.circle(canvas, (255,255,255), (sx,sy), brush)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if drawing:
                ex, ey = mx, my - TH
                if tool == "rect":
                    rw, rh = abs(ex-sx), abs(ey-sy)
                    if rw and rh:
                        pygame.draw.rect(canvas, color, (min(sx,ex),min(sy,ey),rw,rh), brush//2+1)
                if tool == "circle":
                    r = max(abs(ex-sx), abs(ey-sy)) // 2
                    if r: pygame.draw.circle(canvas, color, ((sx+ex)//2,(sy+ey)//2), r, brush//2+1)
            drawing = False

        if event.type == pygame.MOUSEMOTION and drawing and my >= TH:
            cx, cy = mx, my - TH
            if tool == "pencil":
                px2, py2 = mx - event.rel[0], my - event.rel[1] - TH
                if py2 >= 0: pygame.draw.line(canvas, color, (px2,py2), (cx,cy), brush)
                pygame.draw.circle(canvas, color, (cx,cy), brush//2)
            if tool == "eraser":
                pygame.draw.circle(canvas, (255,255,255), (cx,cy), brush)

    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, TH))

    # тулбар
    pygame.draw.rect(screen, (230,230,230), (0,0,SW,TH))
    pygame.draw.line(screen, (100,100,100), (0,TH-1),(SW,TH-1),2)
    for t, bx in TOOLS:
        bg = (80,80,80) if t==tool else (170,170,170)
        pygame.draw.rect(screen, bg, (bx,8,64,34), border_radius=4)
        txt = font.render(t, True, (255,255,255) if t==tool else (0,0,0))
        screen.blit(txt, (bx+(64-txt.get_width())//2, 8+(34-txt.get_height())//2))
    for i, c in enumerate(PALETTE):
        x = 340 + i*33
        pygame.draw.rect(screen, c, (x,10,28,28))
        pygame.draw.rect(screen, (0,0,0), (x,10,28,28), 3 if c==color else 1)
    screen.blit(font.render(f"sz:{brush}", True, (0,0,0)), (SW-60, 17))

    if tool == "eraser":
        pygame.draw.circle(screen, (80,80,80), (mx,my), brush, 1)

    pygame.display.flip()