import time
import random
import math
import sys
import pygame

pygame.init()

pygame_height = 500
pygame_width = 500
fps = 30
pygame_window_name = "Minecraft-py"
screen = pygame.display.set_mode((pygame_width, pygame_height))
pygame.display.set_caption(pygame_window_name)
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
mid_font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 75)

start_screen = True

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

def draw_items():
    boxcolor = (200, 200, 200)
    wood = (237, 174, 0)
    stone = (220, 220, 220)
    pygame.draw.rect(screen, boxcolor, (pygame_width / 5, pygame_height / 5 * 4 + pygame_height / 50 * 4, pygame_width / 10, pygame_width / 10))
    if slot_1 == "wood": # 445
        pygame.draw.rect(screen, wood, (pygame_width / pygame_width * 105, pygame_height / pygame_height * 445, 40, 40))
    elif slot_1 == "stone":
        pygame.draw.rect(screen, stone, (105, 445, 40, 40))
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
    if number == "1":
        slot_1 = item
        slot_1_count = count
    elif number == "2":
        slot_2 = item
        slot_2_count = count
    elif number == "3":
        slot_3 = item
        slot_3_count = count
    elif number == "4":
        slot_4 = item
        slot_4_count = count
    elif number == "5":
        slot_5 = item
        slot_5_count = count
    else:
        print("Function error!")

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
        if start_screen == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if test_text.rect.collidepoint(event.pos):
                    get_item("1", "wood", 1)
    screen.fill((255, 255, 255))
    #pygame.draw.rect(screen, (255, 255, 255), (50, 50, 50, 50))
    if start_screen == True:
        screen.blit(title_text.text, (title_text.posx, title_text.posy))
        screen.blit(start_text.text, (start_text.posx, start_text.posy))
    if start_screen == False:
        draw_items()
        screen.blit(test_text.text, (test_text.posx, test_text.posy))		
    clock.tick(fps)
    pygame.display.update()
