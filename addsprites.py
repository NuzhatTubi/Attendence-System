import pygame

pygame.init()

window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Box Lol")

white=(255,255,255)
blue=(0,0,255)
black=(0,0,0)

#Box 1
b1size=20
b1x=100
b1y=100
b1h=50
b1w=50

#Box 2
b2size=20
b2x=150
b2y=150
b2h=100
b2w=100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        b1x=b1x-10
    if key[pygame.K_RIGHT]:
        b1x=b1x+10
    if key[pygame.K_DOWN]:
        b1x=b1y-10
    if key[pygame.K_UP]:
        b1x=b1x+10

    window.fill(blue)

    pygame.draw.rect(window,white,(b1x,b1y,b1h,b1w))
    pygame.draw.rect(window,white,(b2x,b2y,b2h,b2w))

    
    pygame.display.flip()




pygame.quit()