import random

CELL_SIZE = 20

class SnakeSegment:
	x = 10
	y = 10
	direction = RIGHT

	def render(self):
		# TODO change the color OR change the rect to an image
		fill(0, 0, 255)
		rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

	def move(self):
		if self.direction == LEFT:
			self.x = self.x - 1
		if self.direction == RIGHT:
			pass #TODO fill this in
		
		# TODO repeat for UP and DOWN


class Food:
	x = 20
	y = 10

	# TODO write a render method for the Food, just like for the SnakeSegment



# initialize the snake list and food here
snake_list = [SnakeSegment()]
leader_direction = snake_list[0].direction
my_food = Food()


# The next few functions don't require any changes
def is_over():
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

def keyPressed():
	global leader_direction
	if keyCode in [LEFT, RIGHT, UP, DOWN]:
		leader_direction = keyCode

def setup():
	size(750, 750)
	background(0)
	frameRate(15)


# Lots to do here!
def draw():
	setup()

	# get the new direction
	leader = snake_list[0]

	# set all the segments going in the right direction
	backwards_items = reversed(snake_list)
	backwards_list = list(backwards_items)
	for index, segment in enumerate(backwards_list):
		if segment == leader:
			# TODO set the segment's direction to leader_direction
			pass
		else:
			segment_in_front = backwards_list[index + 1]
			# TODO set the segment's direction to the segment_in_front's direction
			pass


	new_segment = None

	# if we've eaten the food, do the right thing
	# TODO change the if statement on the next line to check if the leader is at the same coordinates as my_food
	if True:
		# TODO move the food to a random location

		# add a new segment
		new_segment = SnakeSegment()
		new_segment.x = backwards_list[0].x
		new_segment.y = backwards_list[0].y


	# TODO render my_food (outside of the if statement)
	

	# TODO write a for loop through each segment in the snake_list
	# inside the loop, move each segment and then render each segment

	# add the new segment if we have one
	if new_segment:
		snake_list.append(new_segment)
		print len(snake_list) + 1


	# TODO if is_over(), write some text saying "DEAD!"

