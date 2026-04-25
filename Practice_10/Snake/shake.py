import pygame, random, sys

pygame.init()
CELL, COLS, ROWS = 20, 30, 25
W, H = COLS * CELL, ROWS * CELL

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

snake = [(COLS//2, ROWS//2)]
dx, dy = 1, 0
score = 0
game_over = False


def new_food():
    while True:
        p = random.randint(0, COLS-1), random.randint(0, ROWS-1)
        if p not in snake:
            return p

food = new_food()

while True:
    clock.tick(7)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                snake = [(COLS//2, ROWS//2)]
                dx, dy = 1, 0
                score = 0
                food = new_food()
                game_over = False
            if event.key == pygame.K_UP    and dy != 1:  dx, dy = 0, -1
            if event.key == pygame.K_DOWN  and dy != -1: dx, dy = 0,  1
            if event.key == pygame.K_LEFT  and dx != 1:  dx, dy = -1, 0
            if event.key == pygame.K_RIGHT and dx != -1: dx, dy =  1, 0

    if not game_over:
        hx, hy = snake[0][0] + dx, snake[0][1] + dy
        hx, hy = hx % COLS, hy % ROWS
        if (hx, hy) in snake:
            game_over = True
        else:
            snake.insert(0, (hx, hy))
            if (hx, hy) == food:
                score += 10
                food = new_food()
            else:
                snake.pop()

    screen.fill((20, 20, 20))

    for x, y in snake:
        pygame.draw.rect(screen, (50, 200, 50), (x*CELL+2, y*CELL+2, CELL-4, CELL-4))

    pygame.draw.rect(screen, (220, 50, 50), (food[0]*CELL+2, food[1]*CELL+2, CELL-4, CELL-4))

    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))

    if game_over:
        t = font.render("GAME OVER  |  R - заново", True, (255, 80, 80))
        screen.blit(t, (W//2 - t.get_width()//2, H//2))

    pygame.display.flip()