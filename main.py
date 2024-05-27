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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit by forcequit")
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, (255, 255, 255), (50, 50, 50, 50))
    clock.tick(fps)
    pygame.display.update()
