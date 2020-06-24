cnt = 0
for a in range(1,150):
    for b in range(1,150):
            pow = a ** b
            l = len(str(pow))
            if l == b:
                    print (str(a) + " ** " + str(b) + " = " + str(a ** b) + " => len = " + str(l))
                    cnt = cnt + 1

print ("cnt = " + str(cnt))
