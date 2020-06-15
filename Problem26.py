from decimal import *
import math

PREC = 3000
getcontext().prec = PREC

def isPrime(n):
	for d in range(2, n):
		if n % d == 0:
			return False;
	return True;

maxLen = 0
maxLenNum = 0
for d in range(1000, 11, -1):
	if isPrime(d):
		print (str(d) + " | curr state {maxLenNum=" + str(maxLenNum) + ", maxLen=" + str(maxLen) + "}")
		div = Decimal(1) / Decimal(d)
		divStr = str(div)	
		# print ("1/" + str(d) + " -> " + divStr + "\n")
		prod10 = 1
		divProd10 = 0
		for i in range(1,PREC):
			prod10 = pow(10, i)
			divProd10 = Decimal(prod10) / Decimal(d)
			l = PREC - i + 2
			# print (str(i) + " -> int(" + str(int(divProd10)) + ") -> [dp10 - dstr] = " + str(divProd10 - Decimal(divStr[0:l])))
			if int(divProd10) == Decimal(str(divProd10 - Decimal(divStr[0:l]))[:-1]):
				break
		# print ("\n" + str(int(divProd10)))
		# break
		if len(str(int(divProd10))) > maxLen:
			maxLen = len(str(int(divProd10)))
			maxLenNum = d

print (maxLenNum)
print (maxLen)
print (Decimal(1) / Decimal(maxLenNum))
		
