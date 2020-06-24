
factArr = [ 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 ]
def factorial(n):
	return factArr[n]

def digitFactSum(n):
	sum = 0
	while n > 0:
		d = n % 10
		n = n / 10
		sum = sum + factorial(d)
	return sum


MAX = 999
MAX_SUM = len(str(MAX)) * factorial(9)
while MAX < MAX_SUM:
	MAX = MAX * 10 + 9
	MAX_SUM = MAX_SUM + factorial(9)
	print ("MAX = " + str(MAX) + ", MAX_SUM = " + str(MAX_SUM))


n = 10
sum = 0
while n <= MAX:
	if n % 100000 == 0:
		print ("reached n = " + str(n))
	if n == digitFactSum(n):
		print (n)
		sum = sum + n
	n = n + 1
print ("final sum = " + str(sum))
