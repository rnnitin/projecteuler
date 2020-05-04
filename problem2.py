sum = 2
x1 = 1
x2 = 2
while x2 < 4000001:
    x3 = x2
    x2 = x2 + x1
    x1 = x3
    if x2 % 2 == 0:
            sum = sum + x2

print (sum)
