import math

prod = 1
for i in range(1,100):
	prod = prod * i

print ("100! = " + str(prod))
strProd = str(prod)

digitSum = 0
for c in strProd:
	digitSum = digitSum + int(c)

print ("digitSum = " + str(digitSum))
