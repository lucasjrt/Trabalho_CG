import pygame

screen_size = (800, 600)

#Cores
white=(255,255,255)
black=(0,0,0)

#Variaveis de estilo
background = white
foreground = black

pygame.init()
screen = pygame.display.set_mode(screen_size)
layer = pygame.surface.Surface(screen_size)
layer.blit(screen, (0,0)) 

pygame.display.set_caption('Trabalho computacao grafica')
screen.fill(background)
layer.fill(white)
pygame.display.flip()

def colorir(x, y, color, overlay=screen):
    overlay.set_at((x,y),color)
    if(overlay.get_at((x,y-1)) == white): colorir(x,y-1,color)
    if(overlay.get_at((x+1,y)) == white and screen_size[0] > x): colorir(x+1,y,color)
    if(overlay.get_at((x,y+1)) == white and screen_size[1] > y): colorir(x,y+1,color)
    if(overlay.get_at((x-1,y)) == white): colorir(x-1,y,color)

def _linhaH(x0, y0, x1, y1, color=foreground, overlay=screen):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0
    for x in range(dx):
        overlay.set_at((x + x0, y), color)
        if D > 0:
           y = y + yi
           D = D - 2*dx
        D = D + 2*dy



def _linhaV(x0, y0, x1, y1, color=foreground, overlay=screen):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0
    for y in range(dy):
        overlay.set_at((x, y + y0), color)
        if D > 0:
            x = x + xi
            D = D - 2*dy
        D = D + 2*dx


def _segmento(x0, y0, x1, y1, color=foreground, overlay=screen):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            _linhaH(x1, y1, x0, y0, color, overlay)
        else:
            _linhaH(x0, y0, x1, y1, color, overlay)
    else:
        if y0 > y1:
            _linhaV(x1, y1, x0, y0, color, overlay)
        else:
            _linhaV(x0, y0, x1, y1, color, overlay)


def linha(x0, y0, x1, y1, color):
    _segmento(x0, y0, x1, y1, color)
    pygame.display.flip()


def circulo(x0, y0, r, color=foreground, overlay=screen):
    x = 0
    y = r
    d = 1 - r
    _circulo (x, y, x0, y0, color, screen)
    while y > x :
        if d < 0 :
            d = d + ( 2 * x ) + 3
        else:
            d = d + 2 * ( x - y ) + 5
            y = y - 1
        x = x + 1
        _circulo(x, y, x0, y0, color, overlay)
    pygame.display.flip()
    

def _circulo(x, y, x0, y0, color=foreground, overlay=screen):
    overlay.set_at((x + x0, y + y0), color)
    overlay.set_at((x0 - y, x + y0), color)
    overlay.set_at((x0 - y, y0 - x), color)
    overlay.set_at((x0 - x, y0 - y), color)
    overlay.set_at((x0 - x, y + y0), color)
    overlay.set_at((x + x0, y0 - y), color)
    overlay.set_at((y + x0, y0 - x), color)
    overlay.set_at((y + x0, x + y0), color)


def retangulo(x, y, w, h, color=foreground, overlay=screen):
    _segmento(x, y, w, y, color, overlay)
    _segmento(w, y, w, h, color, overlay)
    _segmento(w, h, x, h, color, overlay)
    _segmento(x, h, x, y, color, overlay)
    pygame.display.flip()


def triangulo(x, y, size, color=foreground, overlay=screen):
    _segmento(x - size, y + size, x, y - size, color, overlay)
    _segmento(x, y - size, x + size,  y + size, color, overlay)
    _segmento(x + size, y + size, x - size, y + size, color, overlay)
    pygame.display.flip()


'''def curva(x, y, x0, y0, color=foreground, overlay=screen):
	for t in numpy.arange(0,1,0.01):
    omt  = 1-t
    omt2 = omt*omt	
    omt3 = omt2*omt		
    t2   = t*t
    t3   = t2*t
    x    = omt3 * p1[0] + ((3*omt2)*t*p1[0]) + (3*omt*t2*p3[0])+t3*p4[0]
    y    = omt3 * p1[1] + ((3*omt2)*t*p1[1]) + (3*omt*t2*p3[1])+t3*p4[1]
    x    = int(numpy.floor(x))
    y    = int(numpy.floor(y))
     
    screen.set_at((x,y), white)
    pygame.display.flip()'''
