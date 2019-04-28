import pygame, sys, math, primitives
from primitives import *
from pynput.mouse import Listener
from pynput import mouse

#Variaveis de controle
clicked = False
start = (0, 0)
primitivas = {'Linha', 'Circulo', 'Retangulo', 'Quadrado', 'Triangulo', 'Curva'} #Apenas para referencia, desnecessario
atual = 0 #Primitiva atual sendo desenhada

#Implementacao da interface
#Esqueleto
linha(screen_size[0] >> 2, 0, screen_size[0] >> 2, screen_size[1], foreground)
for i in range(len(primitivas)):
    y = screen_size[1] // len(primitivas) * (i + 1)
    linha(0, y, screen_size[0] >> 2, y, foreground)
#Desenho amostral das primitivas
#Linha
x0 = screen_size[0] >> 5
y0 = (screen_size[1] // 6) >> 2 
x1 = (screen_size[0] >> 2) - (screen_size[0] >> 5)
y1 = (screen_size[1] // 6) - (screen_size[0] >> 5)
linha(x0, y0, x1, y1, foreground)
#Circulo
x0 = screen_size[0] >> 3 
y0 = (screen_size[1] // 6) + (screen_size[1] // 12)
r = screen_size[1] // 24
circulo(x0, y0, r, foreground)
#Retangulo
x0 = screen_size[0] >> 5
y0 = ((screen_size[1] // 6) >> 2) + (screen_size[1] // 3)
x1 = (screen_size[0] >> 2) - (screen_size[0] >> 5)
y1 = ((screen_size[1] // 6) - (screen_size[0] >> 5)) + (screen_size[1] // 3)# - (screen_size[1] // 6 >> 2))
retangulo(x0, y0, x1, y1, foreground)
#Quadrado
x0 = (screen_size[0] >> 4) + (screen_size[0] >> 5) 
y0 = ((screen_size[1] // 6) * 3) + (screen_size[1] // 24)
size = screen_size[1] // 12
retangulo(x0, y0, x0 + size, y0 + size, foreground)
#Triangulo
x0 = (screen_size[0] >> 3)
y0 = ((screen_size[1] // 6) * 4) + (screen_size[1] // 12)
size = screen_size[1] // 18 
triangulo(x0, y0, size, foreground)
#Curva
#TODO: Depois de implementada a curva, adicionar aqui

layer.blit(screen, (0,0))

#Mouse listeners
def on_move(x, y):
    global start 
    if clicked:
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX < screen_size[0] >> 2:
            mouseX = screen_size[0] >> 2
        screen.blit(layer, (0,0))
        if atual == 0: 
            linha(start[0], start[1], mouseX, mouseY, foreground)
        elif atual == 1:
            r = int(math.sqrt(((mouseX - start[0]) ** 2) + ((mouseY - start[1]) ** 2)))
            if r > start[0] - (screen_size[0] >> 2):
                r = start[0] - (screen_size[0] >> 2)
            circulo(start[0], start[1], r, foreground)
        elif atual == 2:
            retangulo(start[0], start[1], mouseX, mouseY, foreground)
        elif atual == 3:
            signal = abs(mouseY - start[1]) // (mouseY - start[1]) if mouseY != start[1] else 1
            if mouseX < start[0]:
                signal = -signal
            retangulo(start[0], start[1], mouseX, start[1] + ((mouseX - start[0]) * signal), foreground)
        elif atual == 4:
            r = int(math.sqrt(((mouseX - start[0]) ** 2) + ((mouseY - start[1]) ** 2)))
            if r > start[0] - (screen_size[0] >> 2):
                r = start[0] - (screen_size[0] >> 2)
            triangulo(start[0], start[1], r, foreground)
        else:
            #TODO: Desenho da curva
            pass


def on_click(x, y, button, pressed):
    global clicked
    global start
    global atual
    mouseX, mouseY = pygame.mouse.get_pos()
    start = (mouseX, mouseY)
    if pressed:
        if mouseX > screen_size[0] >> 2:
            clicked = True
        else: #Fora do viewport
            atual = mouseY // (screen_size[1] // len(primitivas))
    else:
        clicked = False
        layer.blit(screen, (0,0))


listener = mouse.Listener( on_move=on_move, on_click=on_click)
listener.start()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

