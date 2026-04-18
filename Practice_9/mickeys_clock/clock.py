import pygame
import math

class MickeysClock:
    def __init__(self, screen_width, screen_height):
        self.cx = screen_width // 2   # Center x
        self.cy = screen_height // 2  # Center y
        # Load Mickey's hand image
        try:
            self.hand_img = pygame.image.load("images/mickey_hand.png").convert_alpha()
        except FileNotFoundError:
            self.hand_img = None  # Fallback: draw lines

    def _draw_hand(self, surface, angle_deg, length, color, width):
        """Draw a clock hand as a line (fallback if no image)."""
        # 0° = 12 o'clock, rotate clockwise
        angle_rad = math.radians(angle_deg - 90)
        end_x = self.cx + length * math.cos(angle_rad)
        end_y = self.cy + length * math.sin(angle_rad)
        pygame.draw.line(surface, color, (self.cx, self.cy),
                         (int(end_x), int(end_y)), width)

    def _draw_hand_image(self, surface, image, angle_deg):
        """Rotate and blit the Mickey hand image."""
        rotated = pygame.transform.rotate(image, -angle_deg)
        rect = rotated.get_rect(center=(self.cx, self.cy))
        surface.blit(rotated, rect)

    def draw(self, surface, minutes, seconds):
        # Angles: 360° / 60 units = 6° per unit
        minute_angle = minutes * 6       # 0–354°
        second_angle = seconds * 6       # 0–354°

        if self.hand_img:
            # Scale versions for minute and second hands
            minute_hand = pygame.transform.scale(self.hand_img, (30, 120))
            second_hand = pygame.transform.scale(self.hand_img, (20, 100))
            # Right hand = minutes
            self._draw_hand_image(surface, minute_hand, minute_angle)
            # Left hand = seconds (mirror for left hand feel)
            left_hand = pygame.transform.flip(second_hand, True, False)
            self._draw_hand_image(surface, left_hand, second_angle)
        else:
            # Fallback: draw simple lines
            self._draw_hand(surface, minute_angle, 100, (0, 0, 200), 8)   # Blue = minutes
            self._draw_hand(surface, second_angle, 120, (200, 0, 0), 4)   # Red = seconds

        # Center dot
        pygame.draw.circle(surface, (0, 0, 0), (self.cx, self.cy), 6)