import pygame
import sys

pygame.init()

#initial window dimensions
window = (720,720)

#window renderer
screen = pygame.display.set_mode(window)

#Game Loop for each event
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

#change window color
