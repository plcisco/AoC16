import hashlib
input = 'ojvtpuvg'
counter, index=0, 0
code=['*','*','*','*','*','*','*','*']
while True:
	m = hashlib.md5()
	m.update(input+str(index))
	index+=1
	hash = m.hexdigest()
	if hash[:5] == '00000':
		print hash
		if (int(hash[5],16)<8):
			if (code[int(hash[5],16)] == '*'):
				code[int(hash[5])]=str(hash[6])
				counter+=1
				print code
		if counter == 8: break