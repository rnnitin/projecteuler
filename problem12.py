import sys
import math

def cntFactors(n):
    cnt = 0
    m = int(math.sqrt(n))
    for i in range(1,m+1):
        if n % i == 0:
            if (n / i == i):
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt

for n in range(10,100000):
    t = n * (n+1) / 2
    cnt = cntFactors(t)
    if cnt > 500:
        print (t)
        break
