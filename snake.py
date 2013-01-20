import random

CELL_SIZE = 20

class SnakeSegment:
	x = 10
	y = 10
	direction = RIGHT

	def render(self):
		fill(0, 0, 255)
		rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

	def move(self):
		if self.direction == LEFT:
			self.x -= 1
		if self.direction == RIGHT:
			self.x += 1
		if self.direction == UP:
			self.y -= 1
		if self.direction == DOWN:
			self.y += 1


class Food:
	x = 20
	y = 10

	def render(self):
		fill(0, 255, 0)
		rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)


snake_list = [SnakeSegment()]
leader_direction = snake_list[0].direction
my_food = Food()

# requires access to a global named snake_list
def is_overlap():
	leader = snake_list[0]
	if leader.x * CELL_SIZE > width or leader.x < 0 or leader.y * CELL_SIZE > height or leader.y < 0:
		print "off the board"
		return True

	for segment1 in snake_list:
		for segment2 in snake_list:
			if segment1 == segment2:
				continue

			if segment1.x == segment2.x and segment1.y == segment2.y:
				return True

	return False

def setup():
	size(750, 750)
	background(0)
	frameRate(15)

def keyPressed():
	global leader_direction
	if keyCode in [LEFT, RIGHT, UP, DOWN]:
		leader_direction = keyCode

def draw():
	setup()

	# get the new direction
	leader = snake_list[0]

	# set all the segments going in the right direction
	backwards_items = reversed(snake_list)
	backwards_list = list(backwards_items)
	for index, segment in enumerate(backwards_list):
		if segment == leader:
			segment.direction = leader_direction
		else:
			segment.direction = backwards_list[index + 1].direction


	new_segment = None
	# if we've eaten the food, do the right thing
	if leader.x == my_food.x and leader.y == my_food.y:
		# move the food to a random location
		my_food.x = random.randint(2, (width - CELL_SIZE) / CELL_SIZE)
		my_food.y = random.randint(2, (height - CELL_SIZE) / CELL_SIZE)

		# add a new segment
		new_segment = SnakeSegment()
		new_segment.x = backwards_list[0].x
		new_segment.y = backwards_list[0].y

		print len(snake_list) + 1

	# render the food
	my_food.render()

	# move and render all the pieces of the snake list
	for segment in snake_list:
		segment.move()

		# is there an overlap?
		if is_overlap():
			print "Dead"
			fill(255)
			textSize(50)
			text("DEAD", 100, 100)
			return

		segment.render()

	# add the new segment if we have one
	if new_segment:
		snake_list.append(new_segment)
	

