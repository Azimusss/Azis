import sys
import pygame
import os
from Classes import Vector

FPS = 40
RESX = 800
RESY = 600

NORMAL = 0
TURN_LEFT = 1
TURN_RIGHT = 2
ACCEL = 3
SPEED_DOWN = 4


class Ship:
    def __init__(self, pos):
        self.pos = Vector(pos)
        self.image = pygame.Surface((100, 100))
        self.accel = 0.2                                    # Acceleration speed
        self.old_speed = None
        self.speed = Vector((1, 0))
        self.state = NORMAL
        self.draw()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.state = TURN_LEFT
            if event.key == pygame.K_RIGHT:
                self.state = TURN_RIGHT
            if event.key == pygame.K_UP:
                self.state = ACCEL
            if event.key == pygame.K_DOWN:
                self.state = SPEED_DOWN
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.KEYUP:
            self.state = NORMAL

    def update(self):
        if self.state == TURN_LEFT:
            rl = -7
            self.speed = self.speed.rotate(rl)
        if self.state == TURN_RIGHT:
            rr = 7
            self.speed = self.speed.rotate(rr)
        if self.state == ACCEL:                         # Ускорение
            if self.speed.len == 0:
                self.speed = self.old_speed
            else:
                self.speed += self.speed.normalize()
        if self.speed.len == 0:
            return
        if self.state == SPEED_DOWN:                       # Остановка
            if self.speed.len > self.accel:
                self.speed -= self.speed.normalize()
            else:
                self.old_speed = self.speed
                self.speed = Vector((0, 0))                 # Обнуление вектора скорости
        self.pos += self.speed

    def draw(self):
        pygame.draw.polygon(self.image, (200, 0, 150), [(3, 7), (5, 5), (7, 5), (10, 2), (14, 2), (15, 3), (18, 3),
                                                        (18, 4), (15, 4), (15, 5), (13, 7), (13, 8), (16, 8),
                                                        (16, 9), (20, 9), (20, 11), (16, 11), (16, 12), (13, 12),
                                                        (13, 13), (15, 15), (15, 16), (18, 16), (15, 17), (15, 17),
                                                        (14, 18), (10, 18), (7, 15), (5, 15), (3, 13)])
        self.image = pygame.transform.scale(self.image, (200, 200))

    def render(self, screen):
        screen.blit(self.image, self.pos.as_point())
        pygame.draw.line(screen, (0, 255, 0), (self.pos + Vector((20, 20))).as_point(), (self.pos + self.speed*25 + Vector((20, 20))).as_point())
        font = pygame.font.SysFont("Courier New", 12)
        text = font.render('%0.4f' % self.speed.len, 2, (0, 250, 0))
        screen.blit(text, (RESX - text.get_rect().w, 20))
pygame.init()
pygame.display.set_mode((RESX, RESY))
screen = pygame.display.get_surface()
ship = Ship((100, 100))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        ship.events(event)
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(FPS)
    ship.update()
    screen.fill((0, 0, 0))
    ship.render(screen)
    pygame.display.flip()