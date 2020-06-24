import math

v = int(math.pow(2, 1000))
vs = str(v)
print ("2^1000 = " + vs)
sum = 0
for ch in vs:
    if ch == '.':
        break
    sum = sum + int(ch)
print (str(sum))
