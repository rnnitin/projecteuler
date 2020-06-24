def isLychrel(n):
	for itr in range (0,50):
		nStr = str(n)
		rnStr = nStr[::-1]
		rn = int(rnStr)
		nrnStr = str(n + rn)
		if nrnStr == nrnStr[::-1]:
			return False
		n = int(nrnStr)
	return True


numLychrels = 0
for n in range(10,10000):
	if isLychrel(n):
		numLychrels = numLychrels + 1

print ("numLychrels below 10000 is " + str(numLychrels))