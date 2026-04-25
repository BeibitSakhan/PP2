import pygame, random, sys, os

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

px, py = 180, 500
enemies = []
coins = []
score = 0
coin_count = 0
speed = 4
game_over = False

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                os.execv(sys.executable, [sys.executable] + sys.argv)
            if event.key == pygame.K_q:
                pygame.quit(); sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]  and px > 60:        px -= 5
        if keys[pygame.K_RIGHT] and px < 300:       px += 5

        if random.randint(1, 60) == 1:
            ex = random.randint(65, 295)
            ec = random.choice([(255,60,60),(60,200,60),(255,160,0)])
            enemies.append([ex, -70, ec])

        for e in enemies: e[1] += speed
        enemies = [e for e in enemies if e[1] < 620]

        if random.randint(1, 90) == 1:
            coins.append([random.randint(75, 325), -13])
        for c in coins: c[1] += speed
        coins = [c for c in coins if c[1] < 620]

        pr = pygame.Rect(px+3, py+3, 34, 64)
        if any(pr.colliderect(pygame.Rect(e[0]+3, e[1]+3, 34, 64)) for e in enemies):
            game_over = True

        for c in list(coins):
            if pr.colliderect(pygame.Rect(c[0]-10, c[1]-10, 20, 20)):
                coins.remove(c); coin_count += 1

        score += 1
        if score % 500 == 0 and speed < 12: speed += 1

    screen.fill((34, 139, 34))
    pygame.draw.rect(screen, (60, 60, 60), (60, 0, 280, 600))
    pygame.draw.line(screen, (255,255,255), (60,0),  (60,600),  3)
    pygame.draw.line(screen, (255,255,255), (340,0), (340,600), 3)

    for e in enemies:
        pygame.draw.rect(screen, e[2], (e[0], e[1], 40, 70))

    for c in coins:
        pygame.draw.circle(screen, (255, 215, 0), (c[0], c[1]), 10)

    pygame.draw.rect(screen, (30, 120, 255), (px, py, 40, 70))

    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (8, 8))
    ct = font.render(f"Coins: {coin_count}", True, (255, 215, 0))
    screen.blit(ct, (400 - ct.get_width() - 8, 8))

    if game_over:
        t = font.render("GAME OVER  |  R / Q", True, (220, 50, 50))
        screen.blit(t, (200 - t.get_width()//2, 280))

    pygame.display.flip()