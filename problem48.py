sum = 0
for i in range(1,1001):
	sum = sum + i**i
print (sum)
strSum = str(sum)
print ("last 10 digits is " + strSum[-10:])	
