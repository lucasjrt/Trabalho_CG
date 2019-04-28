import pygame, sys, math, primitives
from pygame import gfxdraw
from primitives import *
from pynput.mouse import Listener
from pynput import mouse


#Variavel de controle
clicked = False
start = (0, 0)

#primitives.screen.set_at((100, 150), white)
#circulo(100, 150, 102, white)

def on_move(x, y):
    mouseX, mouseY = pygame.mouse.get_pos()
    global start 
    if clicked:
        primitives.screen.fill(white)
        #print('Drawing rectangle of color: ', black)
        #retangulo(start[0], start[1], mouseX, mouseY, black)
        #linha(start[0], start[1], mouseX, mouseY, black)
        r = int(math.sqrt(((mouseX - start[0]) ** 2) + ((mouseY - start[1]) ** 2)))
        triangulo(start[0], start[1], r, black)
        #circulo(start[0], start[1], r, black)

def on_click(x, y, button, pressed):
    global clicked
    global start
    mouseX, mouseY = pygame.mouse.get_pos()
    start = (mouseX, mouseY)
    if pressed:
        clicked = True
    else:
        clicked = False
#    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
#    if not pressed:
#        return False

listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click)
listener.start()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

