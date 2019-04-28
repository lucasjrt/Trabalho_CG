import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Trabalho computacao grafica')
screen.fill((0,0,0))
pygame.display.flip()

#Cores
white=(255,255,255)

#def linha(x1, y1, x2, y2, color):
#    screen.set_at((x1, y1), color)
#    dx = x2 - x1
#    dy = y2 - y1
#    dy2 = 2 * dy
#    dydx2 = dy2 - 2 * dx
#    pant = dy2 - dx
#    x = x1
#    y = y1
#    for i in range(dx):
#        if pant < 0:
#            screen.set_at((x + 1, y), color)
#            pant = pant + dy2
#        else:
#            screen.set_at((x + 1, y + 1), color)
#            pant = pant + dydx2
#            y += 1
#        x += 1
#    pygame.display.flip()


def _linhaH(x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0

    for x in range(dx):
        screen.set_at((x + x0, y), color)
        if D > 0:
            y = y + yi
            D = D - 2*dx

        D = D + 2*dy

def _linhaV(x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0

    for y in range(dy):
        screen.set_at((x, y + y0), white)
        if D > 0:
            x = x + xi
            D = D - 2*dy
        D = D + 2*dx


def _segmento(x0, y0, x1, y1, color):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            _linhaH(x1, y1, x0, y0, color)
        else:
            _linhaH(x0, y0, x1, y1, color)
    else:
        if y0 > y1:
            _linhaV(x1, y1, x0, y0, color)
        else:
            _linhaV(x0, y0, x1, y1, color)

def linha(x0, y0, x1, y1, color):
    _segmento(x0, y0, x1, y1, color)
    pygame.display.flip()

def circulo(x0, y0, r, color):
    x = 0
    y = r
    d = 1 - r
 
    _circulo (x, y, x0, y0, color)
    while y > x :
        if d < 0 :
            d = d + ( 2 * x ) + 3
        else:
            d = d + 2 * ( x - y ) + 5
            y = y - 1
        x = x + 1
        _circulo(x, y, x0, y0, color)
    pygame.display.flip()
    

def _circulo(x, y, x0, y0, color):

    screen.set_at((x + x0, y + y0), color)
    screen.set_at((x0 - y, x + y0), color)
    screen.set_at((x0 - y, y0 - x), color)
    screen.set_at((x0 - x, y0 - y), color)
    screen.set_at((x0 - x, y + y0), color)
    screen.set_at((x + x0, y0 - y), color)
    screen.set_at((y + x0, y0 - x), color)
    screen.set_at((y + x0, x + y0), color)



def retangulo(x, y, w, h, color):
    _segmento(x, y, w, y, white)
    _segmento(w, y, w, h, white)
    _segmento(w, h, x, h, white)
    _segmento(x, h, x, y, white)
    pygame.display.flip()



#linha(10 + 50, 10 + 50, 50 + 50, 50 + 50)
#circulo(200, 200, 100, white)
#retangulo(10, 10, 100, 100, white)

#while 1:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            sys.exit()

