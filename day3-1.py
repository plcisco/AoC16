triangles = open('d3-1-input.txt', 'r').readlines()
number = 0
for sizes in triangles:
	sortedlist = sorted(map(int, sizes.split()), key=int)
	if sortedlist[2] < sortedlist[0]+sortedlist[1]: number+=1
print number