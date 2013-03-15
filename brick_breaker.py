WIDTH = 400
HEIGHT = 600

###### A Paddle has an x coordinate, y coordinate, width, and height.  It has a render method to draw it ######

class Paddle:
	x = WIDTH / 2
	y = HEIGHT - 50
	w = 70
	h = 15
	def render(self):
		rect(self.x, self.y, self.w, self.h)

###### A Ball has an x coordinate, y coordinate, v_x, and v_y.  
###### v_x is the x-direction it's headed.  v_x is 1 if the ball is going right, or -1 if the ball is going left
###### v_y is the y-direction.  v_y is 1 if the ball is going down, or -1 if the ball is going up
###### it also has a render method that draws the Ball and moves it to the next location

class Ball:
	radius = 10
	x = 200
	y = 300
	v_x = 1
	v_y = 1
	speed_multiplier = 5

	def render(self):
		ellipse(self.x, self.y, self.radius, self.radius)

		# how do we move it to the next location?
		self.x = self.x + self.v_x * self.speed_multiplier
		self.y += self.v_y * self.speed_multiplier

class Brick:
	x = 10
	y = 10
	width = 20
	height = 10

	def render(self):
		rect(self.x, self.y, self.width, self.height)

############### TODO ###############
# create a ball named ball1 and a ball named ball2
# set their x coordinates to different places on the screen.
# remember, to create an object, write: my_object_name = Ball()
# then to set a property (in this case, y), write: my_object_name.y = 20



bricks = []

for i in range(1, 10):
	for j in range(1, 3):
		new_brick = Brick()
		new_brick.x = 2 * new_brick.width * i
		new_brick.y = 2 * new_brick.height * j
		bricks.append(new_brick)


############### TODO ###############
# create a Paddle object named my_paddle



def hit_test(ball):
	############### TODO ###############

	# if the ball's x coordinate is on the left wall (<= 0), make the ball head back to the right

	# if the ball's x coordinate is on the right wall (>= WIDTH), make the ball head back to the left

	# if the ball hits the top, make the ball head back down
	

	# the following code checks if the ball hits the paddles or the bricks.  don't worry about it.
	# ball has to be between the top and bottom of the paddle
	# ball has to be between the left and right of the paddle
	if ball.y >= my_paddle.y - ball.radius / 2 and \
		ball.y <= my_paddle.y + my_paddle.h + ball.radius / 2 and \
		ball.x >= my_paddle.x - ball.radius / 2 and \
		ball.x <= my_paddle.x + my_paddle.w + ball.radius / 2:

		############### TODO ###############
		# the ball hit the paddle.  reverse the ball's v_y


	# check every brick
	for br in bricks:
		if ball.y >= br.y and \
			ball.y <= br.y + br.height and \
			ball.x >= br.x and \
			ball.x <= br.x + br.width:

			bricks.remove(br)

			############### TODO ###############
			# the ball hit a brick.  reverse the ball's v_y



def setup():
	size(WIDTH, HEIGHT)
	background(0, 0, 0)

def draw():
	setup()
	############### TODO ###############
	# render ball1 and ball2 by calling their render methods

	# then execute the hit_test for both balls

	# then render the paddle

	# set the paddle's x coordinate to mouseX, the x coordinate of the mouse

	# loop over every individual_brick in bricks
		# render each individual_brick