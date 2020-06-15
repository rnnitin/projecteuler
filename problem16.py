
twoPowerThousand = pow(2, 1000)
twoPowerThousandStr = str(twoPowerThousand)
digitsSum = 0
for c in twoPowerThousandStr:
    if c < '0' or c > '9':
        break
    digitsSum = digitsSum + int(c)
print digitsSum
