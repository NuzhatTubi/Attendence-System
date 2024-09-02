import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("color changing boxes :3")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)

class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.color = color

    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)

sprite1 = MySprite((255, 0, 0), 100, 100, 150, 250)
sprite2 = MySprite((0, 0, 255), 100, 100, 550, 250)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill(WHITE)

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
