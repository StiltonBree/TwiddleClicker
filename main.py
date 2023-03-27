import pygame
import sys


pygame.init()

#initial window dimensions
window = (720,720)
#window renderer
screen = pygame.display.set_mode((window))

#bool for running to avoid video errors
running = True

#font from sysfont
font = pygame.font.SysFont('comicsansms',30)

#button color
buttonColor = (70,80,90)
#Game Loop for each event
# adding sys.exit gets rid of the video system not initialized error
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,55))
    
    mouse = pygame.mouse.get_pos()
    
    pygame.draw.circle(screen,buttonColor, (360,520), 80.0)
    pygame.display.update()