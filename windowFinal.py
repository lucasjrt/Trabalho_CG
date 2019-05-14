import pygame, sys, math, primitives
from primitives import *
from pynput.mouse import Listener
from pynput.keyboard import Key, Listener
from pynput import mouse
from threading import Thread

#Variaveis de curva
selected_point = None
curving = False
#control_points = [(300,100), (300,500), (450,500), (500,150)]
control_points = [(0,0),(0,0),(0,0)]
#Variaveis de controle
clicked = False
start = (0, 0)
primitivas = {'Linha', 'Circulo', 'Retangulo', 'Quadrado', 'Polilinha', 'Curva'} #Apenas para referencia, desnecessario
cores = [(255,255,254),(51,51,51),(255,0,0),(255,51,51),(255,255,0),(0,255,0),(0,230,255),(0,80,255),(255,0,255),(255,160,10),(255,10,160),(10,255,120),(130,130,130),(0,0,0),(0,0,255),(255,200,10)]
atual = 0 #Primitiva atual sendo desenhada
atualcor = 0 #Cor atual sendo usada
c = 0
#Implementacao da interface
#Esqueleto
linha(screen_size[0] >> 2, 0, screen_size[0] >> 2, screen_size[1], foreground)#viewport left
linha(screen_size[0] >> 2, screen_size[1] >> 4,screen_size[0], screen_size[1] >> 4,foreground)# viewport top
for i in range((screen_size[0] >> 2) + 10, (screen_size[0] >> 2) + 538, 33):
    retangulo(i, 3, i+29, 32, foreground)
    colorir(i+1,4,cores[c])
    c = c+1
for i in range(len(primitivas)):
    y = screen_size[1] // len(primitivas) * (i + 1)
    linha(0, y, screen_size[0] >> 2, y, foreground)
retangulo((screen_size[0] >> 2) + 556, 5, (screen_size[0] >> 2) + 581, 30,foreground)
retangulo((screen_size[0] >> 2) + 561, 10, (screen_size[0] >> 2) + 576, 25,foreground)
colorir((screen_size[0] >> 2) + 563,12,cores[atualcor])

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
x0 = screen_size[0] >> 5
y0 = ((screen_size[1] // 6) * 5) + 24
x1 = (screen_size[0] >> 2) - 24 
y1 = screen_size[1] - 24
x2 = (screen_size[0] >> 2) - 24 
y2 = ((screen_size[1] // 6) * 5) + 24
bezierQuadrado((x0,y0),(x1,y1),(x2,y2))
#TODO: Depois de implementada a curva, adicionar aqui

layer.blit(screen, (0,0))

#Mouse listeners
def on_move(x, y):
    global control_points
    global start
    global atual
    global clicked
    global curving
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
        elif atual == 5:
            if curving == 1:
                linha(start[0], start[1], mouseX, mouseY, foreground)
            elif curving == 2:
                bezierQuadrado(control_points[0], control_points[1], (mouseX,mouseY))
            else:
                curving = 0
            '''
            for p in control_points:
                if selected_point is not None:
                    if selected_point is not None:
                        control_points[selected_point] = (mouseX, mouseY)
                        circulo(control_points[selected_point][0], control_points[selected_point][1], 10, (0,255,0))
                    # Desenha os pontos de controle
                    for p in control_points:
                        circulo(p[0], p[1], 4, (0,0,255))

                    # Desenha as linhas de controle
                    #for i in range(0,len(control_points)-1):
                    linhaSegmento(control_points[0][0], control_points[0][1], control_points[1][0], control_points[1][1], (200,200,200))
                    linhaSegmento(control_points[2][0], control_points[2][1], control_points[3][0], control_points[3][1], (200,200,200))

                    # Desenha a curva de bezier
                    b_points = bezierCubica([(x[0], x[1]) for x in control_points])
                    for i in range(0,len(b_points)-1):
                        linhaSegmento(b_points[i][0], b_points[i][1], b_points[i+1][0], b_points[i+1][1], (255,0,0))
                    pygame.display.flip()
            '''
        else:
            pass
            #floodfill


def on_click(x, y, button, pressed):
    global selected_point
    global control_points
    global clicked
    global start
    global atual
    global atualcor
    global curving
    mouseX, mouseY = pygame.mouse.get_pos()
    start = (mouseX, mouseY)
    if pressed:
        if atual != 5: layer.blit(screen, (0,0))
        if mouseX > screen_size[0] >> 2 and mouseY > screen_size[1] >> 4:
            if atual == 5:
                clicked = True
                if curving == 0:
                    control_points[curving] = (mouseX,mouseY)
                    curving = curving + 1
                elif curving == 1:
                    control_points[curving] = (mouseX,mouseY)
                    curving = curving + 1
                elif curving == 2:
                    control_points[curving] = (mouseX,mouseY)
                    curving = curving + 1
                    layer.blit(screen, (0,0))
                else:
                    clicked = False
                '''
                if atual == 5:
                if curving:
                    index = 0
                    for p in control_points:
                        if abs(p[0] - start[0]) < 10 and abs(p[1] - start[1]) < 10 :
                            selected_point = index
                        index = index + 1
                    clicked = True
                else:
                    # Desenha os pontos de controle
                    for p in control_points:
                        circulo(p[0], p[1], 4, (0,0,255))

                    # Desenha as linhas de controle
                    #for i in range(0,len(control_points)-1):
                    linhaSegmento(control_points[0][0], control_points[0][1], control_points[1][0], control_points[1][1], (200,200,200))
                    linhaSegmento(control_points[2][0], control_points[2][1], control_points[3][0], control_points[3][1], (200,200,200))

                    # Desenha a curva de bezier
                    b_points = bezierCubica([(x[0], x[1]) for x in control_points])
                    for i in range(0,len(b_points)-1):
                        linhaSegmento(b_points[i][0], b_points[i][1], b_points[i+1][0], b_points[i+1][1], (255,0,0))
                    pygame.display.flip()
                    curving = True'''
            elif atual == 6:
                colorir(mouseX,mouseY,cores[atualcor])
                pygame.display.flip()
            else:
                clicked = True
        elif mouseX < screen_size[0] >> 2: #Dentro do menu
            atual = mouseY // (screen_size[1] // len(primitivas))
            if atual == 5:
                curving = 0
                print(curving)
        elif mouseX > (screen_size[0] >> 2) + 556 and mouseY > 5 and mouseX < (screen_size[0] >> 2) + 581 and mouseY < 30:
            atual = 6
        else:
            c = 0
            for i in range((screen_size[0] >> 2) + 10, (screen_size[0] >> 2) + 538, 33):
                if mouseX > i and mouseY > 3 and mouseX < i+29 and mouseY < 32:
                    atualcor = c
                    colorir((screen_size[0] >> 2) + 563,12,cores[atualcor])
                    
                    break
                c = c+1
    else:
        if atual != 4 and atual != 5:
            layer.blit(screen, (0,0))
            clicked = False


def on_press(key):
    global clicked
    global atual
    if key == Key.esc:
        clicked = False
        screen.blit(layer, (0,0))
    '''if key == Key.enter:
        if atual == 5:
            #b_points = compute_bezier_points([(x[0], x[1]) for x in control_points])
            for i in range(0,len(b_points)-1):
                linhaSegmento(b_points[i][0], b_points[i][1], b_points[i+1][0], b_points[i+1][1], (255,0,0))
            pygame.display.flip()
            layer.blit(screen, (0,0))'''


listener = mouse.Listener( on_move=on_move, on_click=on_click)
listener.start()

def kb_listener(args):
    global on_press
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
