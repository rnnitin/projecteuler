primes = []

def sortString(str): 
    return ''.join(sorted(str)) 

def genPrimes():
	for k in range(3,10000):
		sqrtK = 1+int(k ** 0.5)
		isPrime = True
		for p in primes:
			if p >= sqrtK:
				break
			if k % p == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(k)

dict1 = {}
dict2 = {}
def main():
	if len(primes) == 0:
		primes.append(2)
		genPrimes()
	for p in primes:
		pStr = str(p)
		sortedPStr = sortString(pStr)
		#print ("sortedPStr = " + sortedPStr)
		if sortedPStr in dict1:
			dict1[sortedPStr].append(p)
		else:
			dict1[sortedPStr] = [p]
	for k in dict1:
		v = dict1[k]
		if len(v) >= 3:
			isArithmaticProgression = True
			# dict2 = {}
			for idx1 in range(0,len(v)-1):
				for idx2 in range(1,len(v)):
					d = v[idx2] - v[idx1]
					if d > 0:
						np = d + v[idx2]
						if np in v:
							print (v[idx1],v[idx2],d+v[idx2])

main()