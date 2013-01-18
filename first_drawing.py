import random

def draw_house(x, y, w, h):
	red = 0
	blue = 0
	green = random.randint(0, 256)

	fill(red, green, blue)
	rect(x, y, w, h)
	triangle(x, y, x + w / 2, y - h / 2, x + w, y)

def setup():
	# our code
	size(500, 500)
	background(50, 100, 4) #r, g, b

def draw():
	# called CONTINUOUSLY!!!!!
	if mousePressed:
		draw_house(mouseX, 
					mouseY, 
					random.randint(30, 50), 
					random.randint(30, 50))

	if keyPressed and key == ' ':
		setup()