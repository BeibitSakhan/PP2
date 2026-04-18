import pygame
import sys
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

font_large = pygame.font.SysFont("Courier", 22)
font_small = pygame.font.SysFont("Courier", 16)

player = MusicPlayer("music")

def draw_ui():
    screen.fill((36, 32, 56))
    title = font_large.render("Music Player", True, (255, 255, 255))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    track_text = font_large.render(player.current_track_name(), True, (100, 200, 255))
    screen.blit(track_text, (WIDTH // 2 - track_text.get_width() // 2, 90))

    status = "Playing..." if player.is_playing else "Stopped"
    status_color = (0, 255, 100) if player.is_playing else (255, 80, 80)
    status_surf = font_large.render(status, True, status_color)
    screen.blit(status_surf, (WIDTH // 2 - status_surf.get_width() // 2, 140))

    controls = [
        "P = Play    S = Stop",
        "N = Next      B = Previous",
        " Q = Quit"
    ]
    for i, line in enumerate(controls):
        hint = font_small.render(line, True, (180, 180, 180))
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 200 + i * 25))

    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    draw_ui()
    clock.tick(30)