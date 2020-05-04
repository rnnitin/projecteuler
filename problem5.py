import math
primes = [2, 3, 5, 7, 11, 13, 17, 19]
counts = [0, 0, 0, 0, 0, 0, 0, 0]
for n in range(1,21):
    for i in range(0, len(primes)):
        p = primes[i]
        if n % p == 0:
           pw = int(math.log(n) / math.log(p)) 
           print (str(n) + " = " + str(p) + " ^ " + str(pw))
           if pw > counts[i]:
               counts[i] = pw

lcm = 1
print (primes)
print (counts)
for i in range(0, len(primes)):
	lcm = lcm * math.pow(primes[i], counts[i])
print (lcm)
