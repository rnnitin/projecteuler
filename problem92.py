
def digitSqSum(n):
    sum = 0
    while n > 0:
        d = n % 10
        sum = sum + d*d
        n = n / 10
    return sum

MAX = 10000000
sdc = {89}
for i in range(2,MAX):
    sdsi = i
    if i % 100000 == 0:
        print ("Got to " + str(i))
    sdc1 = {sdsi}
    while sdsi not in sdc and sdsi > 1:
        sdsi = digitSqSum(sdsi)
        sdc1.add(sdsi)
    if sdsi > 1:
        sdc.update(sdc1)
print ("total count that reach 89 till MAX " + str(MAX) + " is: " + str(len(sdc)))
