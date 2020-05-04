import math

# Primes below 10 = [2, 3, 5, 7]
sum=17
n = 9 
while n < 2000000:
    mx = int(math.sqrt(n)) + 1
    isPrime = True
    for d in range(3,mx,2):
       if n % d == 0:
           isPrime = False
           break 
    if isPrime:
        sum = sum + n
    n = n + 2
    if n % 10 == 5:
        n = n + 2
print (sum)
