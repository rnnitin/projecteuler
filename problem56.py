
def digitSum(n):
	sum = 0
	while n > 0:
		sum = sum + n %10
		n = n / 10
	return sum

maxSum = -1
maxA = -1
maxB = -1
for a in range(1,100):
	if a % 5 == 0:
		print (a)
	for b in range (1,100):
		sum = digitSum(a ** b)
		if sum > maxSum:
			maxSum = sum
			maxA = a
			maxB = b
print ("maxSum = " + str(maxSum) + " for a = " + str(maxA) + " & b = " + str(maxB))
