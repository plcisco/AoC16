file = open("d1-1-input.txt", "r")
instructions = file.read().split(', ')

y=0 
x=0
orientation_y=1
orientation_x=0
visited=["00"]
SecondVisit=False


for instruction in instructions:
	if instruction[0] == "L":
		orientation_y_old=orientation_y
		orientation_y=orientation_x
		orientation_x=-1*orientation_y_old
	else:
		orientation_y_old=orientation_y
		orientation_y=-1*orientation_x
		orientation_x=orientation_y_old

	for i in range(1,int(instruction[1:])+1):
		if orientation_y <> 0:
			y+=orientation_y
		else:
			x+=orientation_x	
		if str(x)+str(y) in visited:
			print abs(x)+abs(y)
			SecondVisit=True
			break
		else:
			visited.append(str(x)+str(y))
	if SecondVisit:
		break
