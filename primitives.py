import pygame, numpy

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

def colorir(x, y, cor, overlay=screen):
	stack = [(x,y)]
	atual = (x,y)
	color = overlay.get_at((x,y))
	while stack:
		overlay.set_at((stack[-1]), cor)
		atual = stack[-1]
		stack.pop()
		if atual[0] < screen_size[0] - 1 and atual[1] < screen_size[1] - 1 and overlay.get_at((atual[0] + 1, atual[1])) == color:
			stack.append((atual[0] + 1, atual[1]))

		if atual[0] < screen_size[0] - 1 and atual[1] < screen_size[1] - 1 and overlay.get_at((atual[0] - 1, atual[1])) == color:
			stack.append((atual[0] - 1, atual[1]))

		if atual[0] < screen_size[0] - 1 and atual[1] < screen_size[1] - 1 and overlay.get_at((atual[0], atual[1] + 1)) == color:
			stack.append((atual[0], atual[1] + 1))

		if atual[0] < screen_size[0] - 1 and atual[1] < screen_size[1] - 1 and overlay.get_at((atual[0], atual[1] - 1)) == color:
			stack.append((atual[0], atual[1] - 1))
	#corRecursao(x,y,cor,overlay.get_at((x,y)))
	#pygame.display.flip()


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


def segmento(x0, y0, x1, y1, color=foreground, overlay=screen):
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

#linha(x, y, x, y, cor, layer)

def linha(x0, y0, x1, y1, color, overlay=screen):
	segmento(x0, y0, x1, y1, color, overlay)
	pygame.display.flip()


def linhaSegmento(x0, y0, x1, y1, color):
    segmento(x0, y0, x1, y1, color)


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
	segmento(x, y, w, y, color, overlay)
	segmento(w, y, w, h, color, overlay)
	segmento(w, h, x, h, color, overlay)
	segmento(x, h, x, y, color, overlay)
	pygame.display.flip()


def triangulo(x, y, size, color=foreground, overlay=screen):
	segmento(x - size, y + size, x, y - size, color, overlay)
	segmento(x, y - size, x + size,  y + size, color, overlay)
	segmento(x + size, y + size, x - size, y + size, color, overlay)
	pygame.display.flip()


def compute_bezier_points(vertices, numPoints=None):
	if numPoints is None:
		numPoints = 30
	if numPoints < 2 or len(vertices) != 4:
		return None

	result = []

	b0x = vertices[0][0]
	b0y = vertices[0][1]
	b1x = vertices[1][0]
	b1y = vertices[1][1]
	b2x = vertices[2][0]
	b2y = vertices[2][1]
	b3x = vertices[3][0]
	b3y = vertices[3][1]

	# Compute polynomial coefficients from Bezier points
	ax = -b0x + 3 * b1x + -3 * b2x + b3x
	ay = -b0y + 3 * b1y + -3 * b2y + b3y
	bx = 3 * b0x + -6 * b1x + 3 * b2x
	by = 3 * b0y + -6 * b1y + 3 * b2y
	cx = -3 * b0x + 3 * b1x
	cy = -3 * b0y + 3 * b1y
	dx = b0x
	dy = b0y

	# Set up the number of steps and step size
	numSteps = numPoints - 1 # arbitrary choice
	h = 1.0 / numSteps # compute our step size

	# Compute forward differences from Bezier points and "h"
	pointX = dx
	pointY = dy
	firstFDX = ax * (h * h * h) + bx * (h * h) + cx * h
	firstFDY = ay * (h * h * h) + by * (h * h) + cy * h
	secondFDX = 6 * ax * (h * h * h) + 2 * bx * (h * h)
	secondFDY = 6 * ay * (h * h * h) + 2 * by * (h * h)
	thirdFDX = 6 * ax * (h * h * h)
	thirdFDY = 6 * ay * (h * h * h)

	# Compute points at each step
	result.append((int(pointX), int(pointY)))
	
	for i in range(numSteps):
		pointX += firstFDX
		pointY += firstFDY
		firstFDX += secondFDX
		firstFDY += secondFDY
		secondFDX += thirdFDX
		secondFDY += thirdFDY
		result.append((int(pointX), int(pointY)))
	print(result)
	return result

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


def bezierCubica(vertices, numPoints=None):
	if numPoints is None:
		numPoints = 30
	if numPoints < 2 or len(vertices) != 4:
		return None

	result = []

	b0x = vertices[0][0]
	b0y = vertices[0][1]
	b1x = vertices[1][0]
	b1y = vertices[1][1]
	b2x = vertices[2][0]
	b2y = vertices[2][1]
	b3x = vertices[3][0]
	b3y = vertices[3][1]

	# Compute polynomial coefficients from Bezier points
	ax = -b0x + 3 * b1x + -3 * b2x + b3x
	ay = -b0y + 3 * b1y + -3 * b2y + b3y
	bx = 3 * b0x + -6 * b1x + 3 * b2x
	by = 3 * b0y + -6 * b1y + 3 * b2y
	cx = -3 * b0x + 3 * b1x
	cy = -3 * b0y + 3 * b1y
	dx = b0x
	dy = b0y

	# Set up the number of steps and step size
	numSteps = numPoints - 1 # arbitrary choice
	h = 1.0 / numSteps # compute our step size

	# Compute forward differences from Bezier points and "h"
	pointX = dx
	pointY = dy
	firstFDX = ax * (h * h * h) + bx * (h * h) + cx * h
	firstFDY = ay * (h * h * h) + by * (h * h) + cy * h
	secondFDX = 6 * ax * (h * h * h) + 2 * bx * (h * h)
	secondFDY = 6 * ay * (h * h * h) + 2 * by * (h * h)
	thirdFDX = 6 * ax * (h * h * h)
	thirdFDY = 6 * ay * (h * h * h)

	# Compute points at each step
	result.append((int(pointX), int(pointY)))

	for i in range(numSteps):
		pointX += firstFDX
		pointY += firstFDY
		firstFDX += secondFDX
		firstFDY += secondFDY
		secondFDX += thirdFDX
		secondFDY += thirdFDY
		result.append((int(pointX), int(pointY)))

	return result

def bezierQuadrado(p1,p2,p3):
	for t in numpy.arange(0,1,0.001):
		omt  = 1-t
		omt2 = omt*omt
		t2   = t*t
		x = p1[0] * omt2 + 2 * t * omt * p3[0] + t2 * p2[0] 
		y = p1[1] * omt2 + 2 * t * omt * p3[1] + t2 * p2[1]
		#x    = omt3 * p1[0] + ((3*omt2)*t*p1[0]) + (3*omt*t2*p3[0])+t3*p4[0]
		#y    = omt3 * p1[1] + ((3*omt2)*t*p1[1]) + (3*omt*t2*p3[1])+t3*p4[1]
		x    = int(numpy.floor(x))
		y    = int(numpy.floor(y))

		screen.set_at((x,y), black)
	pygame.display.flip()

