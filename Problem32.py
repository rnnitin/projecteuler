

for i in range(987,123,-1):
	s = str(i)
	if "0" in s:
		continue

        arr = [0,0,0,0,0,0,0,0,0]
	cont = False
	for a in range(len(s)):
		if arr[int(s[a]) - 1] >= 1:
			cont = True
			break
		else:
			arr[int(s[a]) - 1] = 1
	if cont:
		continue

	#print (arr)
	for j in range (1,98):
		cont = False
		sj = str(j)
		if "0" in sj:
			continue
		for a in range(len(sj)):
			if arr[int(sj[a]) - 1] >= 1:
				cont = True
				break
			else:
				arr[int(sj[a]) - 1] = 1
		if cont:
			continue

		prod = i * j
		s = str(prod)
		for a in range(len(s)):
			if arr[int(s[a]) - 1] >= 1:
				cont = True
				break
			else:
				arr[int(s[a]) - 1] = 1
		if cont:
			continue
		#print (arr)

		print (str(i) + " x " + str(j) + " = " + str(prod)); 
		
