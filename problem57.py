dArr = [2,5,12]
for i in range (3,1000):
	d = dArr[i-1]*2 + dArr[i-2]
	print (d)
	dArr.append(d)