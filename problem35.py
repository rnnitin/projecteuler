primes = [2, 3, 5, 7, 11, 13, 17, 19]
count = 7

def isPrime(n):
    if n in primes:
        return True

    m = int(n ** 0.5)
    #print ("n = " + str(n) + ", m = " + str(m))
    for idx in range(0,len(primes)):
        d = primes[idx]
        if d > m:
            break
        if n % d == 0:
            return False
    return True

def isAllOddDigits(n):
    while (n > 0):
        if ( n % 10 ) % 2 == 0:
            return False
        n = n / 10
    return True

def rotate(n):
    return int(str(n % 10) + str(n / 10));


def areAllRotationsPrime(n):
	n1 = rotate(n)
	while n1 != n:
	    if not isPrime(n1):
	    	return False
	    n1 = rotate(n1)
	return True

for n in range (21, 1000000, 2):
    if isPrime(n):
        primes.append(n)
        if isAllOddDigits(n) and areAllRotationsPrime(n):
            print (n)
            count = count + 1
print ("Count = " + str(count))
