# for 2x2 grid the combinations are 2Rs and 2Ds of these if I choose either the Rs or the Ds the other is fixed, so it turns to be 4c2 = 6
# same way for a 20x20 grid the combinations will be of 20 Rs & 20 Ds I can choose 20 of either, which is 40 c 20
# that is 40!/20!*(40-20)!
import math
print (math.factorial(40)/(math.factorial(20)*math.factorial(20)))
