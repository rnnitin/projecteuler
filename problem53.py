def ncr(n,r):
	nprod = 1
	for k in range(r+1,n+1):
		nprod = nprod * k
	nrprod = 1
	for k in range(2,n-r+1):
		nrprod = nrprod * k
	return nprod/nrprod

countNCROver1M = 0
for n in range (23,101):
	for r in range(0,n):
		ncrVal = ncr(n,r)
		if ncrVal > 1000000:
			countNCROver1M = countNCROver1M + 1

print (countNCROver1M)