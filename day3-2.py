triangles = open('d3-1-input.txt', 'r').readlines()
for i in range(0, len(triangles)):
	triangles[i] = map(int, triangles[i].split())
number = 0

for column in range(0,3):
	for i in range(0, (len(triangles)/3)):
		sortedlist = sorted([triangles[i*3][column], triangles[(i*3)+1][column], triangles[(i*3)+2][column]], key=int)
		if sortedlist[2] < sortedlist[0]+sortedlist[1]: number+=1
print number