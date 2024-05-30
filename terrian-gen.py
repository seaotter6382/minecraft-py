import pygame
import random
import time
import math
import sys

py_x = 500
py_y = 500

fps = 30
py_name = "terrian testing"
screen = pygame.display.set_mode((py_x, py_y))
pygame.display.set_caption(py_name)
clock = pygame.time.Clock()

block_x = 0
block_y = 0

block_size = 20
num_blocks_x = py_x // block_size
num_blocks_y = py_y // block_size
layer = 1

generated = False

def ter(type):
    if type == 1: ## stone
        block = random.randint(1, 10)
        if block <= 8:
            return (200, 200, 200)
        if block > 8:
            return (255, 162, 0)
    if type == 2: ## grass
        return (20, 100, 0)
        
def gen():
    global layer
    for x in range(num_blocks_x):
        layer += 1
        for y in range(num_blocks_y):
            if layer < 20:
                terrain_type = random.randint(2, 2)
            if layer >= 20:
                terrain_type = random.randint(1, 1)
            block_x = x * block_size
            block_y = y * block_size
            pygame.draw.rect(screen, ter(terrain_type), (block_x, block_y, block_size, block_size))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit by forcequit")
            pygame.quit()
            sys.exit()
        
    clock.tick(fps)

    gen()
    if generated == False:
        pygame.display.update()
        generated = True
