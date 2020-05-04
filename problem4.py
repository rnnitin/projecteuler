max=-1
Imax=-1
Jmax=-1
for i in range(999,100,-1):
    for j in range(999,100,-1):
	p = i * j
	pStr = str(p)
	if pStr == pStr[::-1]:
	    if max < p:
                max = p
                Imax = i
                Jmax = j
            break
print (str(max) + " = " + str(Imax) + " * " + str(Jmax))
