import pygame

pygame.init()

pygame.mouse.set_cursor(*pygame.cursors.arrow)

screen = pygame.display.set_mode((800, 450))
caption = pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()

color = (255, 255, 255)

screen.fill(color)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(60)
