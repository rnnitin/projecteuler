import time

current_milli_time = lambda: int(round(time.time() * 1000))


primes = [2,3,5,7,11,13,17,19]

def genPrimesTill1M():
	for n in range(20, 1000000):
		sqrtN = int(n ** 0.5)
		isPrime = True
		for p in primes:
			if p > sqrtN:
				break
			if n % p == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(n)

def getPrimeFactors(n):
	primeFactors = []
	for p in primes:
		if p > n:
			break
		if n % p == 0:
			primeFactors.append(p)
	return primeFactors


def phi(n, primeFactors):
	numNonCoPrimes = 0
	# print ("factors of " + str(n) + " = " + str(primeFactors))
	for k in range(2,n):
		for p in primeFactors:
			if p > k:
				break
			if k % p == 0:
				numNonCoPrimes = numNonCoPrimes + 1
				break
	# print ("numNonCoPrimes for " + str(n) + " = " + str(numNonCoPrimes))
	return n - 1 - numNonCoPrimes



def phiNew(n, primeFactors):
	numCoPrimes = 1
	combSet = []
	coPrimePrimes = []
	for p in primes:
		if p < n and p not in primeFactors:
			coPrimePrimes.append(p)
	numCoPrimes = numCoPrimes + len(coPrimePrimes)
	for m in range(1,20):
		for p in coPrimePrimes:
			pow = p ** m
			if pow < n:
				combSet.append(pow)
	# print ("combSet = " + str(combSet))
	for k in combSet:
		for l in combSet:
			if (l * k) >= n:
				break
			numCoPrimes = numCoPrimes + 1
	return numCoPrimes


def nbyphi(n, primeFactors):
	phiVal = phi(n, primeFactors)
	return float(n) / phiVal

def main():
	maxNbyPhi = -1
	nAtMaxNByPhi = 0
	maxNumPrimeFactors = -1
	genPrimesTill1M()
	startTS = current_milli_time()
	itrStrtTS = startTS
	for n in range(MIN,MAX):
		if n % 25000 == 0:
			cTS = current_milli_time()
			print (str(cTS - startTS) + " >>> n = " + str(n) + "; itr TS Diff = " + str(cTS - itrStrtTS))
			itrStrtTS = cTS
		# print (str(n) + " -> " + str(phi(n)) + " -> " + str(nbyphi(n)))
		primeFactors = getPrimeFactors(n)
		if maxNumPrimeFactors < len(primeFactors):
			maxNumPrimeFactors = len(primeFactors)
			nByPhi = nbyphi(n, primeFactors)
			if nByPhi > maxNbyPhi:
				maxNbyPhi = nByPhi
				nAtMaxNByPhi = n
	print ("n = " + str(nAtMaxNByPhi) + " -> nByPhi = " + str(maxNbyPhi))

MIN = 2
MAX = 1000000
main()