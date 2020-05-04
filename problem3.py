import math

max=int(math.sqrt(600851475143))
if max % 2 == 0:
    max = max - 1
if max % 5 == 0:
    max = max - 2

for i in range(max, 3, -2):
    if i % 10 == 5:
        continue
    if 600851475143 % i == 0:
         mx = int(math.sqrt(i))
         j = 3
         while j <= mx:
             if i % j == 0:
                 break;
             else:
                 j = j + 2 
                 if j % 10 == 5:
                     j = j + 2
         if j > mx - 10:
             print (i)
             break
