file = open("d1-1-input.txt", "r")
instructions = file.read().split(', ')

y=0 
x=0
orientation_y=1
orientation_x=0

for instruction in instructions:
	if instruction[0] == "L":
		orientation_y_old=orientation_y
		orientation_y=orientation_x
		orientation_x=-1*orientation_y_old
	else:
		orientation_y_old=orientation_y
		orientation_y=-1*orientation_x
		orientation_x=orientation_y_old
	y+=orientation_y*int(instruction[1:])
	x+=orientation_x*int(instruction[1:])

print abs(x)+abs(y)