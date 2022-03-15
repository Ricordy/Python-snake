import pygame
import time
import random

pygame.init()
display_x = 600
display_y = 500
display = pygame.display.set_mode((display_x,display_y))
pygame.display.update()
pygame.display.set_caption("Snake")


blue=(0,0,255)
red=(255,0,0)
white=(0, 0, 0)
yellow = (0, 255, 255)








clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)


def snake_list(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, blue, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_x/2, display_y/2])

def gameSnake():

    is_finished = False
    x = display_x /2
    y = display_y /2
    x_change = 0
    y_change = 0
    s_block_x = 10
    s_block_y = 10
    point_x = round(random.randrange(0, display_x - s_block_x) / 10.0) * 10.0
    point_y = round(random.randrange(0, display_y - s_block_y) / 10.0) * 10.0
    snakes = []
    snake_length  = 1
    snake_speed = 1

    while not is_finished:
        
        for event in pygame.event.get():
            
            
            #If quit or close is pressed
            if (event.type == pygame.QUIT):
                is_finished = True
            
            
            #Moviments
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_UP):
                    print("oi")
                    y_change =  -10 * snake_speed
                    x_change = 0
                elif(event.key == pygame.K_DOWN):
                    y_change =  10 * snake_speed
                    x_change = 0
                elif(event.key == pygame.K_LEFT):
                    x_change =  -10 * snake_speed
                    y_change = 0
                elif(event.key == pygame.K_RIGHT):
                    x_change =  10  * snake_speed
                    y_change = 0


            #Making the move
            x += x_change
            y += y_change
        
            #Display the move 
            pygame.draw.rect(display,blue,[x,y,s_block_x,s_block_y])

            snake_Head = []
            snake_Head.append(x)
            snake_Head.append(y)
            snakes.append(snake_Head)
            if len(snakes) > snake_length:
                del snakes[0]
 
            for xi in snakes[:-1]:
                if xi == snake_Head:
                    is_finished = False

 
            snake_list(s_block_x, snakes)



            pygame.display.update()
            display.fill(white)

            #Draw food
            pygame.draw.rect(display, yellow, [point_x,point_y, 5,5])


            #Eat
            if x == point_x and y == point_y:
                point_x = round(random.randrange(0, display_x - s_block_x) / 10.0) * 10.0
                point_y = round(random.randrange(0, display_y - s_block_y) / 10.0) * 10.0

                snake_length += 1
 



            #Verifies if snake is on boarder
            if x == display_x or x == 0 or y == display_y or y == 0: 
                is_finished = True
            


            clock.tick(10)

gameSnake()


message("You lost",red)
pygame.display.update()
time.sleep(2)
clock.tick(60)
pygame.quit()
quit()
        















