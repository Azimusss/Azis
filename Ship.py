import sys
import pygame
import os
from Classes import Vector

FPS = 40
NORMAL = 0
TURN_LEFT = 1
TURN_RIGHT = 2


class Ship:
    def __init__(self, pos):
        self.pos = Vector(pos)
        self.image = pygame.Surface((100, 100))
        self.speed = Vector((1, 0))
        self.state = NORMAL
        self.draw()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.state = TURN_LEFT
            if event.key == pygame.K_RIGHT:
                self.state = TURN_RIGHT
        if event.type == pygame.KEYUP:
            self.state = NORMAL

    def update(self):
        print("update")
        if self.state == TURN_LEFT:
            self.speed = self.speed.rotate(-5)
        if self.state == TURN_RIGHT:
            self.speed = self.speed.rotate(5)
        self.pos += self.speed

    def draw(self):
        pygame.draw.rect(self.image, (200, 0, 150), (0, 0, 20, 15))

    def render(self, screen):
        screen.blit(self.image, self.pos.as_point())
        pygame.draw.line(screen, (0, 255, 0), self.pos.as_point(), (self.pos + self.speed*20).as_point())


def load_image(name, alpha_cannel):
    fullname = os.path.join('Images', name)  # Указываем путь к папке с картинками

    image = pygame.image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
    if alpha_cannel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


pygame.init()
pygame.display.set_mode((800, 600))
screen = pygame.display.get_surface()

image = load_image('Picture/4.png', 1)  # загружаем картинку. Вторым аргументом указываем (есть/нет) альфа-канал

ship = Ship((20, 100))
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