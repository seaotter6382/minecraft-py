import time
import random
import math
import sys
import pygame
from pygame.locals import *

pygame.init()

pygame_height = 500
pygame_width = 500
fps = 30
pygame_window_name = "Minecraft-py"
screen = pygame.display.set_mode((pygame_width, pygame_height))
pygame.display.set_caption(pygame_window_name)
clock = pygame.time.Clock()

small_font = pygame.font.Font(None, 20)
font = pygame.font.Font(None, 36)
mid_font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 75)

start_screen = True
show_inv = False
Dead = False

frames_up = 0

slot_1 = ""
slot_1_count = 0
slot_2 = ""
slot_2_count = 0
slot_3 = ""
slot_3_count = 0
slot_4 = ""
slot_4_count = 0
slot_5 = ""
slot_5_count = 0

total_health = 10
health = 10
health_regen_rate = 0.5
last_regen_time = time.time()

select_item = 1

class title_text():
    color = (0, 0, 0)
    text = mid_font.render("Minecraft Py", True, color)
    posx = pygame_width * 0.3
    posy = 100

class start_text():
    color = (32, 135, 0)
    text = mid_font.render("Start", True, color)
    posx = pygame_width * 0.4
    posy = pygame_height / 2
    rect = text.get_rect(topleft=(posx, posy))

class test_text():
	color = (0, 0, 0)
	text = mid_font.render("Get wood", True, color)
	posx = pygame_width * 0.33
	posy = pygame_height / 3
	rect = text.get_rect(topleft=(posx, posy))

class health_text():
    color = (0, 0, 0)
    text = mid_font.render("Take Damage", True, color)
    posx = pygame_width * 0.33
    posy = pygame_height / 10
    rect = text.get_rect(topleft=(posx, posy))

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("GREY"))
    screen.blit(fps_t,(0,0))

def draw_items():
    boxcolor = (200, 200, 200)
    wood = (237, 174, 0)
    stone = (220, 220, 220)
    if select_item == 1:
        pygame.draw.rect(screen, (0, 0, 0), (95, 435, 60, 60))
    if select_item == 2:
        pygame.draw.rect(screen, (0, 0, 0), (155, 435, 60, 60))
    if select_item == 3:
        pygame.draw.rect(screen, (0, 0, 0), (215, 435, 60, 60))
    if select_item == 4:
        pygame.draw.rect(screen, (0, 0, 0), (275, 435, 60, 60))
    if select_item == 5:
        pygame.draw.rect(screen, (0, 0, 0), (335, 435, 60, 60))
    pygame.draw.rect(screen, boxcolor, (pygame_width / 5, pygame_height / 5 * 4 + pygame_height / 50 * 4, pygame_width / 10, pygame_width / 10))
    if slot_1 == "wood": 
        pygame.draw.rect(screen, wood, (pygame_width / 5 + pygame_width / 100, 445, 40, 40))
    elif slot_1 == "stone":
        pygame.draw.rect(screen, stone, (105, 445, 40, 40))
    if slot_1_count > 1:
        screen.blit((font.render(str(slot_1_count), True, (100, 100, 100))), (135, 465))
    screen.blit((font.render("1", True, (0, 0, 0))), (100, 440))
    pygame.draw.rect(screen, boxcolor, (160, 440, 50, 50))
    if slot_2 == "wood":
        pygame.draw.rect(screen, wood, (165, 445, 40, 40))
    screen.blit((font.render("2", True, (0, 0, 0))), (160, 440))
    pygame.draw.rect(screen, boxcolor, (220, 440, 50, 50))
    if slot_3 == "wood":
        pygame.draw.rect(screen, wood, (225, 445, 40, 40))
    screen.blit((font.render("3", True, (0, 0, 0))), (220, 440))
    pygame.draw.rect(screen, boxcolor, (280, 440, 50, 50))
    if slot_4 == "wood":
        pygame.draw.rect(screen, wood, (285, 445, 40, 40))
    screen.blit((font.render("4", True, (0, 0, 0))), (280, 440))
    pygame.draw.rect(screen, boxcolor, (340, 440, 50, 50))
    if slot_5 == "wood":
        pygame.draw.rect(screen, wood, (345, 445, 40, 40))
    screen.blit((font.render("5", True, (0, 0, 0))), (340, 440))

def get_item(number, item, count):
    global slot_1, slot_1_count
    global slot_2, slot_2_count
    global slot_3, slot_3_count
    global slot_4, slot_4_count
    global slot_5, slot_5_count
    if number == 1:
        slot_1 = item
        slot_1_count += count
    elif number == 2:
        slot_2 = item
        slot_2_count += count
    elif number == 3:
        slot_3 = item
        slot_3_count += count
    elif number == 4:
        slot_4 = item
        slot_4_count += count
    elif number == 5:
        slot_5 = item
        slot_5_count += count
    else:
        print("Function error!")

def draw_health():
    pygame.draw.rect(screen, (200, 200, 200), (100, 420, total_health * 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), (100, 420, health * 10, 10))

def minus_health(damage):
    global health
    if health == 0:
        print("you dead")
    else:
        health = health - damage

def regen_health():
    global health, last_regen_time
    
    current_time = time.time()
    time_e = current_time - last_regen_time
    if time_e >= 0.5:
        health_to_regen = time_e * health_regen_rate
        health = min(health + health_to_regen, total_health)
        last_regen_time = current_time

def generate():
    x = pygame_width
    y = pygame_height
    xy = x / y

    x2 = x / 10
    y2 = y / 10

    pygame.draw.rect(screen, (200, 200, 200), (x, y, x2, y2))

def draw_death():
    global frames_up
    screen.blit((font.render("Total Frames: " + str(frames_up), True, (0, 0, 0))), (pygame_width / 2, pygame_height / 2))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit by forcequit")
            pygame.quit()
            sys.exit()
        if start_screen == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_text.rect.collidepoint(event.pos):
                    start_screen = False
                    health = 10
        if start_screen == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if test_text.rect.collidepoint(event.pos):
                    get_item(1, "wood", 1)
                elif health_text.rect.collidepoint(event.pos):
                    minus_health(1)
            elif event.type == KEYDOWN:
                if event.key == K_e:
                    print("inventory is now " + str(show_inv))
                    show_inv = not show_inv
                elif event.key == K_1:
                    select_item = 1
                elif event.key == K_2:
                    select_item = 2
                elif event.key == K_3:
                    select_item = 3
                elif event.key == K_4:
                    select_item = 4
                elif event.key == K_5:
                    select_item = 5

    screen.fill((255, 255, 255))
    regen_health()
    frames_up = frames_up + 1

    if start_screen == True:
        screen.blit(title_text.text, (title_text.posx, title_text.posy))
        screen.blit(start_text.text, (start_text.posx, start_text.posy))
    if start_screen == False:
        draw_items()
        screen.blit(test_text.text, (test_text.posx, test_text.posy))
        screen.blit(health_text.text, (health_text.posx, health_text.posy))
        if show_inv == True:
            pygame.draw.rect(screen, (200, 200, 200), (pygame_width / 5, pygame_height / 5, pygame_width / 5 * 3, pygame_width / 5 * 3))
        draw_health()
        generate()
    if dead = True:

    
    if health <= 0:
        print("you dead")
        start_screen = True
        health = 10
        dead = True

    fps_counter()
    clock.tick(fps)
    pygame.display.update()
