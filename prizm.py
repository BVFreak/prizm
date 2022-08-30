# -*- coding: utf-8 -*-
import sys
import pygame
import random
from button import Button

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

BACKGROUND_MENU_IMAGE = pygame.image.load("assets/Background-Menu.png")
BACKGROUND_WORLD_IMAGE = pygame.image.load("assets/background-world.png")

bob_surface = pygame.image.load("assets/bob.png")
bob_surface_left = pygame.transform.flip(bob_surface, True, False)

sound_shoot = pygame.mixer.Sound("assets/audio/pewpew.mp3")
sound_beep1 = pygame.mixer.Sound("assets/audio/beep1.mp3")
sound_beep2 = pygame.mixer.Sound("assets/audio/beep2.mp3")

MUSIC_MAINMENU = "assets/audio/song1.mp3"
MUSIC_MAINMENU1 = "assets/audio/song.mp3"

BACKGROUND_MENU = "black"
BACKGROUND_GAME = "white"
BACKGROUND_SETTINGS = "lightblue"


def get_font(size):  # Returns Font in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    pygame.mixer.music.stop()

    x_position = (width/2)-50
    y_position = (height/2)-50
    x_increment = 2
    y_increment = 2

    x_world_position = -2000
    y_world_position = -2000

    facing_right = True
    flip = False
    bob = bob_surface

    while True:
        screen.fill(BACKGROUND_GAME)

        for event in pygame.event.get():
            pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.play()
            pygame.mixer.Sound.play(sound_beep1)
            return

        # movement
        if keys[pygame.K_d]:
            x_world_position = x_world_position - x_increment

            if not facing_right:
                facing_right = True 
                bob = bob_surface
            
        if keys[pygame.K_a]:
            x_world_position = x_world_position + x_increment

            if facing_right:
                facing_right = False
                bob = bob_surface_left

        if keys[pygame.K_w]:
            y_world_position = y_world_position + y_increment

        if keys[pygame.K_s]:
            y_world_position = y_world_position - y_increment

        # shoot
        if keys[pygame.K_SPACE]:
            pygame.mixer.Sound.play(sound_shoot)

        # sprint
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_d]:
                x_world_position = x_world_position - x_increment
            
            if keys[pygame.K_a]:
                x_world_position = x_world_position + x_increment

            if keys[pygame.K_w]:
                y_world_position = y_world_position + y_increment

            if keys[pygame.K_s]:
                y_world_position = y_world_position - y_increment
            

        screen.blit(BACKGROUND_WORLD_IMAGE, (x_world_position, y_world_position))
        screen.blit(bob, (x_position, y_position))

        pygame.display.update()


def settings():
    while True:
        screen.fill(BACKGROUND_SETTINGS)
        screen.blit(BACKGROUND_MENU_IMAGE, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        SETTINGS_TEXT = get_font(50).render("Controlsrender\nWASD to move\nShift to sprint\nLeft click to attack\nRight click to defend\nEscape to go back to main menu\n\nMade by Blake VernerW\nith special thanks to Anthony Tassonyi, Ruan Verner and David Nugent.\n", True, "#999999")
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(640, 100))

        RETURN_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="DONE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(SETTINGS_TEXT, SETTINGS_RECT)

        for button in [RETURN_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(sound_beep1)
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.Sound.play(sound_beep1)
            return

        pygame.display.update()


def main_menu():
    pygame.mixer.music.stop()
    choice_music = random.randint(1, 2)
    if choice_music == 1:
        pygame.mixer.music.load(MUSIC_MAINMENU)
        pygame.mixer.music.play()
    elif choice_music == 2:
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
                    pygame.mixer.Sound.play(sound_beep1)
                    play()
                if SETTINGS_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(sound_beep1)
                    settings()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.Sound.play(sound_beep1)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
