import pygame

pygame.init()

(width, height) = (800, 450)
screen = pygame.display.set_mode((width, height))
caption = pygame.display.set_caption("Prizm")
clock = pygame.time.Clock()

#Loading Images
bob_surface = pygame.image.load('sprites/bob.png')

x_position = 0
y_position = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            clock.tick(60)


    #Keyboard Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x_position = x_position + 1
    if keys[pygame.K_LEFT]:
        x_position = x_position - 1
    if keys[pygame.K_UP]:
        y_position = y_position - 1
    if keys[pygame.K_DOWN]:
        y_position = y_position + 1
        
    #Background/Drawing Image
    screen.fill((255, 255, 255))
    
    screen.blit(bob_surface,(x_position, y_position))

    pygame.display.update()
