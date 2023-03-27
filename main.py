import pygame
import sys

#importing my button class
import button

pygame.init()

#initial window dimensions
window = (720,720)
#window renderer
screen = pygame.display.set_mode((window))

#bool for running to avoid video errors
running = True

#font from sysfont
font = pygame.font.SysFont('comicsansms',30)

#Game Loop for each event
# adding sys.exit gets rid of the video system not initialized error
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,55))
    pygame.display.update()