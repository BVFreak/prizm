import pygame

pygame.init()

(width, height) = (800, 450)
screen = pygame.display.set_mode((width, height))
caption = pygame.display.set_caption("Prizm")
clock = pygame.time.Clock()

bob_surface = pygame.image.load('sprites/bob.png')

x_position = 0
y_position = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            clock.tick(60)



    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_position = x_position + 0.75
    if keys[pygame.K_a]:
        x_position = x_position - 0.75
    if keys[pygame.K_w]:
        y_position = y_position - 0.75
    if keys[pygame.K_s]:
        y_position = y_position + 0.75
        
    
    screen.fill((255, 255, 255))
    
    screen.blit(bob_surface,(x_position, y_position))

    pygame.display.update()
