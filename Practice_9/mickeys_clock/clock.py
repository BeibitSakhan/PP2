import pygame
import math

class MickeysClock:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = 145
        self.font = pygame.font.SysFont("Arial", 28, bold=True)

        self.min_angle = 0
        self.sec_angle = 0
        self.hour_angle = 0

        try:
            hand = pygame.image.load("images/mickeys_hand.png").convert_alpha()
            self.right_hand = pygame.transform.scale(hand, (40, 130))
            self.hour_hand_img = pygame.transform.scale(hand, (45, 90)) 
            self.has_image = True
        except FileNotFoundError:
            self.has_image = False

    def update(self, hours, minutes):
        self.hour_angle = -((hours % 12) * 30 + minutes * 0.5)
        self.min_angle = -(minutes * 6)

    def draw_ticks(self, screen):
        for i in range(60):
            angle_rad = math.radians(i * 6 - 90)
            if i % 5 == 0:
                start_r = self.radius - 15
                width = 3
            else:
                start_r = self.radius - 8
                width = 1
            sx = self.x + start_r * math.cos(angle_rad)
            sy = self.y + start_r * math.sin(angle_rad)
            ex = self.x + self.radius * math.cos(angle_rad)
            ey = self.y + self.radius * math.sin(angle_rad)
            pygame.draw.line(screen, (0, 0, 0),
                             (int(sx), int(sy)), (int(ex), int(ey)), width)

    def draw_numbers(self, screen):
        for i in range(1, 13):
            angle_rad = math.radians(i * 30 - 90)
            x = self.x + (self.radius - 30) * math.cos(angle_rad)
            y = self.y + (self.radius - 30) * math.sin(angle_rad)
            text = self.font.render(str(i), True, (0, 0, 0))
            screen.blit(text, (int(x - text.get_width() // 2),
                               int(y - text.get_height() // 2)))

    def draw_hand_line(self, screen, angle_deg, length, tail, color, width):
        angle_rad = math.radians(angle_deg - 90)
        ex = self.x + length * math.cos(angle_rad)
        ey = self.y + length * math.sin(angle_rad)
        tx = self.x - tail * math.cos(angle_rad)
        ty = self.y - tail * math.sin(angle_rad)
        pygame.draw.line(screen, color,
                         (int(tx), int(ty)), (int(ex), int(ey)), width)

    def draw(self, screen):
        self.draw_ticks(screen)
        self.draw_numbers(screen)

        if self.has_image:
            # Часовая рука
            hour_rotated = pygame.transform.rotate(self.hour_hand_img, self.hour_angle)
            hour_rect = hour_rotated.get_rect(center=(self.x, self.y))
            screen.blit(hour_rotated, hour_rect.topleft)

            # Минутная — правая рука Микки
            right_hand_rotated = pygame.transform.rotate(self.right_hand, self.min_angle)
            right_rect = right_hand_rotated.get_rect(center=(self.x, self.y))
            screen.blit(right_hand_rotated, right_rect.topleft)

        else:
            # Fallback — линии
            self.draw_hand_line(screen, -self.hour_angle, 90, 20, (0, 0, 0), 10)
            self.draw_hand_line(screen, -self.min_angle, 130, 25, (0, 0, 200), 6)

        # Центральная точка
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 8)
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 4)