# -*- coding: utf-8 -*-
import pygame
import random

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((600, 600))

#title and icon
pygame.display.set_caption("Snake")
icon = pygame.image.load('C:/Users/rohin/Downloads/snake.png')
pygame.display.set_icon(icon)

#clock
clock = pygame.time.Clock()

#velocity and change in position variables
vel = 30
dx = 0
dy = 0

#snake list of x and y coordinates
block_list = []
temp_list = []

#score
score = 1
score_increase = False

class Grid:
    def drawGrid():
        x = 0
        y = 0
        for l in range(30):
            pygame.draw.line(screen, (255, 255, 255), (30 + x, 0), (30 + x, 600), width= 2)
            x += 30
            pygame.draw.line(screen, (255, 255, 255), (0, 0 + y), (600, 0 + y), width = 2)
            y += 30

class Cube:
    def __init__(self, position: list):
        self.position = position
        #position[0] is x coordinate
        #position[1] is y coordinate

    def create_cube(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.position[0], self.position[1], 30, 30))

class Snack:
    def __init__(self, position: list):
        self.position = position

    def create_snack(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], 30, 30))

    def randomize_snack_position(self):
        self.position[0] = 30 * random.randrange(0, 20)
        self.position[1] = 30 * random.randrange(0, 20)

    def eats_snack(): 
        global score, score_increase
        if snake_head.position[0] == s.position[0] and snake_head.position[1] == s.position[1]:
            temp_list.append([0, 0])
            s.randomize_snack_position()  
            score += 1  
            score_increase = True
            
    def check_snack():
        global score_increase
        score_increase = False
        for x in range(len(block_list)):
            if s.position == block_list[x]:
                s.randomize_snack_position()
                print(x)
                x = 0

class Move:               
    def move_snake_head():
        global dx, dy
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                #closing out of window
                pygame.quit()
            if keys[pygame.K_LEFT] and dx != vel:
                dx = -vel
                dy = 0
            if keys[pygame.K_RIGHT] and dx != -vel: 
                dx = vel
                dy = 0
            if keys[pygame.K_UP] and dy != vel: 
                dx = 0
                dy = -vel
            if keys[pygame.K_DOWN] and dy != -vel:
                dx = 0
                dy = vel

    def move_snake_body():
        for x in range(len(temp_list)):
            if x == 0:
                block_list.append(snake_head.position)
            if x == 1:
                if dx == -30:
                    block_list.append([snake_head.position[0] + 30, snake_head.position[1]])
                if dx == 30:
                    block_list.append([snake_head.position[0] - 30, snake_head.position[1]])    
                if dy == -30:
                    block_list.append([snake_head.position[0], snake_head.position[1] + 30])
                if dy == 30:
                    block_list.append([snake_head.position[0], snake_head.position[1] - 30])
            if x > 1:
                block_list.append(temp_list[x-1])

    def collision_check():
        for x in range(len(block_list)):
            if x > 0:
                if snake_head.position == block_list[x]:
                    print("Score:", score)
                    pygame.quit()
        if snake_head.position[0] == -30 or snake_head.position[0] == 600 or snake_head.position[1] == -30 or snake_head.position[1] == 600:
            print("Score:", score)
            pygame.quit()

def main():
    global temp_list, snake_head, s
    snake_head = Cube([300, 300])
    block_list.append(snake_head.position)
    s = Snack([30 * random.randrange(0, 20), 30 * random.randrange(0, 20)])
    run = True
    while run:
        Snack.eats_snack() # randomize snack location, add block, and increase score if snake eats      
        Move.move_snake_head()
        snake_head.position[0] += dx
        snake_head.position[1] += dy
        Move.move_snake_body()  # move the snake
        Move.collision_check() # check if snake collides with itself or the border
        if score_increase == True: #checks if snack position equals new snake position
            Snack.check_snack()
        screen.fill((0,0,0)) #clear the screen
        for x in range(len(block_list)): #recreate the blocks
            if x == 0:
                snake_head.create_cube()
            if x > 0:
                Cube(block_list[x]).create_cube()
        temp_list = block_list[:]
        block_list.clear()
        s.create_snack() #recreate snack
        Grid.drawGrid() #recreact grid
        pygame.display.update()
        clock.tick(10)
        
main()