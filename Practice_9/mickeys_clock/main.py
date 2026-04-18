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
font = pygame.font.SysFont("Arial", 36, bold=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get current time
    now = time.localtime()
    minutes = now.tm_min
    seconds = now.tm_sec

    # Draw background
    screen.fill((255, 240, 200))  # Light warm background

    # Draw clock face circle
    pygame.draw.circle(screen, (255, 255, 255), (WIDTH // 2, HEIGHT // 2), 150)
    pygame.draw.circle(screen, (0, 0, 0), (WIDTH // 2, HEIGHT // 2), 150, 3)

    # Draw clock hands
    mickey_clock.draw(screen, minutes, seconds)

    # Display digital time below
    time_str = f"{minutes:02d}:{seconds:02d}"
    time_surf = font.render(time_str, True, (50, 50, 50))
    screen.blit(time_surf, (WIDTH // 2 - time_surf.get_width() // 2, HEIGHT - 60))

    pygame.display.flip()
    clock_tick.tick(1)  # Update once per second