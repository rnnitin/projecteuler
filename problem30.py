
powArr = [ 0, 1, 2**5, 3**5, 4**5, 5**5, 6**5, 7**5, 8**5, 9**5 ]
def fifthPow(n):
	return powArr[n]

def digit5thPowSum(n):
	sum = 0
	while n > 0:
		d = n % 10
		n = n / 10
		sum = sum + fifthPow(d)
	return sum


MAX = 999
MAX_SUM = len(str(MAX)) * fifthPow(9)
while MAX < MAX_SUM:
	MAX = MAX * 10 + 9
	MAX_SUM = MAX_SUM + fifthPow(9)
	print ("MAX = " + str(MAX) + ", MAX_SUM = " + str(MAX_SUM))


n = 10
sum = 0
while n <= MAX:
	if n % 100000 == 0:
		print ("reached n = " + str(n))
	if n == digit5thPowSum(n):
		print (n)
		sum = sum + n
	n = n + 1
print ("final sum = " + str(sum))
