exitAll = False
for a in range (1,1000):
    if exitAll:
        break
    for b in range (1,1000):
        if exitAll:
            break
        for c in range (1,1000):
           if a + b + c != 1000:
               continue
           if a*a + b*b == c*c:
               print (str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2")
               exitAll = True
               break
print ("prod(a,b,c) = " + str((a-1)*(b-1)*c))
