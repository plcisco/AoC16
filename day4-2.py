import string
codes = open('d4-1-input.txt', 'r').readlines()
total = 0
letters = {}

for code in codes:
	decoded=""
	for char in string.lowercase: letters[char]=0
	parts = code.split('-')
	last = parts.pop()
	chars = ''.join(parts)
	for char in chars: letters[char]+=1
	letlist=letters.items()
	intermediate = sorted(letlist, key=lambda x: x[0])  # needed here. dict.items does not seem to keep the order
	sl = sorted(intermediate, key=lambda x: x[1], reverse=True)
	if (last.split('[')[1][:5] == sl[0][0]+sl[1][0]+sl[2][0]+sl[3][0]+sl[4][0]):
		total+=int(last.split('[')[0])
		for char in chars:
			decoded+=chr(((ord(char)-97+int(last.split('[')[0])) % 26)+97)
		if 'northpoleobjects' in decoded: print last.split('[')[0]
print total