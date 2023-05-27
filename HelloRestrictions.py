import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700, 700), 0, 32)
sprite1 = pygame.image.load('./images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (32, 32))
pygame.display.set_caption("Hello Sprite")
screen.fill((0, 0, 0))
game_over = False
x, y = (0, 0)
clock = pygame.time.Clock()
while not game_over:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()
    speed = 0.5 * dt
    if pressed[K_UP]:
        y -= speed
    if pressed[K_DOWN]:
        y += speed
    if pressed[K_RIGHT]:
        x += speed
    if pressed[K_LEFT]:
        x -= speed
    if pressed[K_SPACE]:
        x, y = (0, 0)
    x = max(min(x, screen.get_width() - sprite1.get_width()), 0)
    y = max(min(y, screen.get_height() - sprite1.get_height()), 0)
    screen.fill((0, 0, 0))
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()
