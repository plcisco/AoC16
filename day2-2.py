instructions = open('d2-1-input.txt', 'r').readlines()
x,y=1,3
layout=[['0','0','0','0','0','0','0'],
		['0','0','0','1','0','0','0'],
		['0','0','2','3','4','0','0'],
		['0','5','6','7','8','9','0'],
		['0','0','A','B','C','0','0'],
		['0','0','0','D','0','0','0'],
		['0','0','0','0','0','0','0']]

for instruction in instructions:
	for i in range(0, len(instruction)):
		if (instruction[i]=='L') & (layout[y][x-1]<>'0'): x-=1
		elif (instruction[i]=='R') & (layout[y][x+1]<>'0'): x+=1
		elif (instruction[i]=='D') & (layout[y+1][x]<>'0'):	y+=1
		elif (instruction[i]=='U') & (layout[y-1][x]<>'0'): y-=1
	print layout[y][x]
