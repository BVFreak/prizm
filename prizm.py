import pygame

BACKGROUND_IMAGE = 'bob.png'
WHITE = (255, 255, 255)

pygame.init()

pygame.mouse.set_cursor(*pygame.cursors.arrow)
screen = pygame.display.set_mode((800, 450))
caption = pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()

# make the background
screen.fill(WHITE)

bg_image = pygame.image.load(BACKGROUND_IMAGE)

screen.blit(bg_image, (0, 0))


pygame.display.flip()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(60)
