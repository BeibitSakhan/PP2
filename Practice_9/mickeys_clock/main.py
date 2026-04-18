import pygame
import sys
import time
from clock import MickeysClock

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")
clock_tick = pygame.time.Clock()

mickey_clock = MickeysClock(WIDTH, HEIGHT)
font = pygame.font.SysFont("Courier", 36, bold=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = time.localtime()
    hours = now.tm_hour    
    minutes = now.tm_min

    mickey_clock.update(hours, minutes)

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 240, 200), (WIDTH // 2, HEIGHT // 2), 150)
    pygame.draw.circle(screen, (0, 0, 0), (WIDTH // 2, HEIGHT // 2), 150, 3)

    mickey_clock.draw(screen)

    time_str = f"{hours:02d}:{minutes:02d}"
    time_surf = font.render(time_str, True, (50, 50, 50))
    screen.blit(time_surf, (WIDTH // 2 - time_surf.get_width() // 2, HEIGHT - 40))

    pygame.display.flip()
    clock_tick.tick(1)