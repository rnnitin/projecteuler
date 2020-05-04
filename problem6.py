sumOfSquares100=0
sum100=100 * 101 / 2
squareOfTheSum100=sum100*sum100
for i in range(1,101):
    sumOfSquares100 = sumOfSquares100 + i * i

print ("diff bet SqOfSum & SumOfSqs is = " + str(squareOfTheSum100 - sumOfSquares100))
