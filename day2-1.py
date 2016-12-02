
file = open("d2-1-input.txt", "r")
instructions = file.readlines()
x=1
y=1
layout = [[1,2,3],
		  [4,5,6],
		  [7,8,9]]

for instruction in instructions:
	for i in range(0, len(instruction)):
		if (instruction[i]=="L") & (x>0):
			x-=1
		elif (instruction[i]=="R") & (x<2):
			x+=1
		elif (instruction[i]=="D") & (y<2):
			y+=1
		elif (instruction[i]=="U") & (y>0):
			y-=1
	print layout[y][x]
