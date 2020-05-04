import math

# first6Primes = [2, 3, 5, 7, 11, 13]
count=6
n = 17
lastSeenPrime=13
while count < 10001:
    mx = int(math.sqrt(n)) + 1
    isPrime = True
    for d in range(3,mx,2):
       if n % d == 0:
           isPrime = False
           break 
    if isPrime:
        count = count + 1
        lastSeenPrime = n
    n = n + 2
    if n % 10 == 5:
        n = n + 2
print (lastSeenPrime)
