import pygame, sys, math, primitives
from primitives import *
from pynput.mouse import Listener
from pynput.keyboard import Key, Listener
from pynput import mouse
from threading import Thread

#Variaveis de controle
clicked = False
start = (0, 0)
primitivas = {'Linha', 'Circulo', 'Retangulo', 'Quadrado', 'Polilinha', 'Curva'} #Apenas para referencia, desnecessario
cores = [(0,0,0),(51,51,51),(255,0,0),(255,51,51),(255,255,0),(0,255,0),(0,230,255),(0,80,255),(255,0,255),(255,160,10),(255,10,160),(10,255,120),(130,130,130),(255,255,254),(0,0,255),(255,200,10)]
atual = 0 #Primitiva atual sendo desenhada
c = 0
#Implementacao da interface
#Esqueleto
linha(screen_size[0] >> 2, 0, screen_size[0] >> 2, screen_size[1], foreground)
linha(screen_size[0] >> 2, screen_size[1] >> 4,screen_size[0], screen_size[1] >> 4,foreground)
for i in range((screen_size[0] >> 2) + 10, (screen_size[0] >> 2) + 538, 33):
    retangulo(i, 3, i+29, 32, foreground)
    colorir(i+1,4,cores[c])
    c = c+1
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
#Polilinha
x0 = (screen_size[0] >> 5)
y0 = ((screen_size[1] // 6) * 5) - screen_size[1] // 24
x1 = (screen_size[0] >> 5) + (screen_size[0] >> 4)
y1 = ((screen_size[1] // 6) * 4) + screen_size[1] // 24
linha(x0, y0, x1, y1, foreground)
x0 = (screen_size[0] >> 3) + (screen_size[0] >> 5)
y0 = ((screen_size[1] // 6) * 5) - screen_size[1] // 24
linha(x1, y1, x0, y0, foreground)
x0 -= 1
y0 += 1
x1 = (screen_size[0] >> 2) - (screen_size[0] >> 5)
y1 = ((screen_size[1] // 6) * 4) + screen_size[1] // 24
linha(x0, y0, x1, y1, foreground)
#Curva
#TODO: Depois de implementada a curva, adicionar aqui

layer.blit(screen, (0,0))

#Mouse listeners
def on_move(x, y):
    global start 
    mouseX, mouseY = pygame.mouse.get_pos()
    if clicked:
        if mouseX < screen_size[0] >> 2:
            mouseX = screen_size[0] >> 2
        if mouseY < screen_size[1] >> 4:
            mouseY = screen_size[1] >> 4
        screen.blit(layer, (0,0))
        if atual == 0: 
            linha(start[0], start[1], mouseX, mouseY, foreground)
        elif atual == 1:
            r = int(math.sqrt(((mouseX - start[0]) ** 2) + ((mouseY - start[1]) ** 2)))
            if r > start[0] - (screen_size[0] >> 2):
                r = start[0] - (screen_size[0] >> 2)
            if r > start[1] - (screen_size[1] >> 4):
                r = start[1] - (screen_size[1] >> 4)
            circulo(start[0], start[1], r, foreground)
        elif atual == 2:
            retangulo(start[0], start[1], mouseX, mouseY, foreground)
        elif atual == 3:
                
            signal = abs(mouseY - start[1]) // (mouseY - start[1]) if mouseY != start[1] else 1
            if mouseX < start[0]:
                signal = -signal

            if abs(mouseX - start[0]) > abs(start[1] - (screen_size[1] >> 4)) and start[1] > mouseY:
                if mouseX > start[0]:
                     mouseX = start[0] + abs((screen_size[1] >> 4) - start[1])
                else:
                     mouseX = start[0] - abs((screen_size[1] >> 4) - start[1])
                
            retangulo(start[0], start[1], mouseX, start[1] + ((mouseX - start[0]) * signal), foreground)
        elif atual == 4:
          	linha(start[0], start[1], mouseX, mouseY, foreground)
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
        layer.blit(screen, (0,0))
        if mouseX > screen_size[0] >> 2 and mouseY > screen_size[1] >> 4:
            clicked = True
        else: #Fora do viewport
            atual = mouseY // (screen_size[1] // len(primitivas))
    else:
        layer.blit(screen, (0,0))
        if atual != 4:
            clicked = False



def on_press(key):
    global clicked
    if key == Key.esc:
        clicked = False
        screen.blit(layer, (0,0))
        pygame.display.flip()


listener = mouse.Listener( on_move=on_move, on_click=on_click)
listener.start()

def kb_listener(args):
    with Listener(on_press=on_press) as l:
        l.join()


thread = Thread(target = kb_listener, args = (10, ))
thread.daemon = True
thread.start()


#try:
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#except SystemExit:
#    pygame.quit()
#    thread.exit()
#    sys.exit()
