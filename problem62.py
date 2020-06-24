def sortString(str): 
    return ''.join(sorted(str)) 

dict = {}
MAX = 10000
for a in range(100,MAX):
    cube = a ** 3
    cubeStr = str(cube)
    sortedCubeStr = sortString(cubeStr)
    if sortedCubeStr in dict:
        dict[sortedCubeStr].append(cubeStr)
    else:
        dict[sortedCubeStr] = [cubeStr]

m = -1
for k in dict:
    v = dict[k]
    if len(v) == 5:
        c = dict[k][0]
        print ("c = " + str(c))
        if c < m or m == -1:
        	m = c
        	print ("min assinged = " + str(m))

print(m)