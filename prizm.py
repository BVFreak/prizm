# -*- coding: utf-8 -*-
from operator import is_
import sys
from telnetlib import AYT
import pygame
from button import Button

pygame.init()

# creates the screen
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Prizm")

# fps cap
clock = pygame.time.Clock()

# menu music
BACKGROUND_MENU_IMAGE = pygame.image.load("assets/Background-Menu.png").convert()
BACKGROUND_WORLD_IMAGE = pygame.image.load("assets/background-world.png").convert()

# bobby
bobby_surface = pygame.image.load("assets/bobby.png").convert_alpha()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.rect.center = pygame.Vector2(*pos)
        self.direction = pygame.Vector2(*direction)

    def update(self):
        self.rect.center += self.direction

bullets = pygame.sprite.Group()

# zombie
zombie_surface = pygame.image.load('assets/dave.png').convert_alpha()

# sounds
sound_shoot = pygame.mixer.Sound("assets/audio/pewpew.mp3")
sound_beep1 = pygame.mixer.Sound("assets/audio/beep1.mp3")
sound_beep2 = pygame.mixer.Sound("assets/audio/beep2.mp3")

# holy music
MUSIC_MAINMENU1 = "assets/audio/song1.mp3"

# menu colours
BACKGROUND_MENU = "black"
BACKGROUND_GAME = "white"
BACKGROUND_SETTINGS = "lightblue"


# menu font
def get_font(size):  # Returns univers condesensed font in the desired size
    return pygame.font.Font("assets/font.ttf", size)

# stops music
def play():
    pygame.mixer.music.stop()
    
    # movement variables
    player_pos = pygame.Vector2((width/2)-50,(height/2)-50)
    zombie_pos = pygame.Vector2((0,0))
    zombie_speed = 0.75
    x_increment = 1
    y_increment = 1

    # world generation size
    x_world_position = -5000
    y_world_position = -5000

    # while true loop
    while True:
        screen.fill(BACKGROUND_GAME)

        for event in pygame.event.get():
            pass

    # returning back to the main menu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.play()
            return

        # movement
        if keys[pygame.K_d]:
            zombie_pos.x -= x_increment
            x_world_position = x_world_position - x_increment
        if keys[pygame.K_a]:
            zombie_pos.x += x_increment
            x_world_position = x_world_position + x_increment
        if keys[pygame.K_w]:
            zombie_pos.y += y_increment
            y_world_position = y_world_position + y_increment
        if keys[pygame.K_s]:
            zombie_pos.y -= y_increment
            y_world_position = y_world_position - y_increment

        # shoot
        if pygame.mouse.get_pressed()[0]:
            dir_to_mouse: pygame.Vector2 = pygame.Vector2(pygame.mouse.get_pos()) - player_pos
            if dir_to_mouse.length() != 0:
                dir_to_mouse.normalize_ip()
            bullet = Bullet(player_pos, dir_to_mouse)
            bullets.add(bullet)

        # sprint
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_d]:
                zombie_pos.x -= x_increment
                x_world_position = x_world_position - x_increment
            if keys[pygame.K_a]:
                zombie_pos.x += x_increment
                x_world_position = x_world_position + x_increment
            if keys[pygame.K_w]:
                zombie_pos.y += y_increment
                y_world_position = y_world_position + y_increment
            if keys[pygame.K_s]:
                zombie_pos.y -= y_increment
                y_world_position = y_world_position - y_increment

        direction: pygame.Vector2 = player_pos - zombie_pos
        if direction.length() != 0:
            direction.normalize_ip()

        zombie_pos += direction * zombie_speed

        screen.blit(BACKGROUND_WORLD_IMAGE, (x_world_position, y_world_position))
        screen.blit(bobby_surface, (player_pos))
        screen.blit(zombie_surface, (zombie_pos))

        bullets.update()
        bullets.draw(screen)
        pygame.display.update()

def settings():
    while True:
        screen.fill(BACKGROUND_SETTINGS)
        screen.blit(BACKGROUND_MENU_IMAGE, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        SETTINGS_TEXT = get_font(75).render("SETTINGS", True, "#999999")
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(640, 100))

        RETURN_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="DONE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(SETTINGS_TEXT, SETTINGS_RECT)

        for button in [RETURN_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return

        pygame.display.update()


def main_menu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSIC_MAINMENU1)
    pygame.mixer.music.play()

    while True:
        screen.fill(BACKGROUND_MENU)
        screen.blit(BACKGROUND_MENU_IMAGE, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("PRIZM", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SETTINGS_BUTTON = Button(image=pygame.image.load("assets/Settings Rect.png"), pos=(640, 400),
                                 text_input="SETTINGS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play()
                if SETTINGS_BUTTON.checkForInput(mouse_pos):
                    settings()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
