import pygame
import sys


pygame.init()

#initial window dimensions
window = (720,720)
#window renderer
screen = pygame.display.set_mode((window))

#dimensions of screen
width = screen.get_width()
height = screen.get_height()

#bool for running to avoid video errors
running = True

#font from sysfont
font = pygame.font.SysFont('comicsansms',30)

#button color
buttonColor = (70,80,90)

text = font.render('Click!', True, (255,255,255))

#Game Loop for each event
# adding sys.exit gets rid of the video system not initialized error
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
                    
    screen.fill((0,0,55))
    
    mouse = pygame.mouse.get_pos()
    
    buttonCircle = pygame.draw.circle(screen,buttonColor, (360,520), 80.0)
    #text over button
    screen.blit(text,(buttonCircle.centerx - 30,buttonCircle.centery - 30))
    pygame.display.update()