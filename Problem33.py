from decimal import *
import math

PREC = 30
getcontext().prec = PREC
SIXPLACES = Decimal(10) ** -6

for n in range (10,100):
	for d in range (10, 100):
		if n == d or n % 10 == 0:
			continue
		n1 = n / 10
		n2 = n % 10
		d1 = d / 10
		d2 = d % 10

		if d1 == n1:
			if d2 != 0 and (Decimal(n) / Decimal(d)).quantize(SIXPLACES) == (Decimal(n2) / Decimal(d2)).quantize(SIXPLACES):
				print (str(n) + "/" + str(d) + " ==> " + str(Decimal(n) / Decimal(d)) + " = " + str(Decimal(n2) / Decimal(d2)))
		else:
			if d2 == n2:
				if d1 != 0 and (Decimal(n) / Decimal(d)).quantize(SIXPLACES) == (Decimal(n1) / Decimal(d1)).quantize(SIXPLACES):
					print (str(n) + "/" + str(d) + " ==> " + str(Decimal(n) / Decimal(d)) + " = " + str(Decimal(n1) / Decimal(d1)))
			else:
				if d1 == n2:
					if d1 != 0 and (Decimal(n) / Decimal(d)).quantize(SIXPLACES) == (Decimal(n2) / Decimal(d1)).quantize(SIXPLACES):
						print (str(n) + "/" + str(d) + " ==> " + str(Decimal(n) / Decimal(d)) + " = " + str(Decimal(n2) / Decimal(d1)))
				else:
					if d2 == n1:
						if d2 != 0 and (Decimal(n) / Decimal(d)).quantize(SIXPLACES) == (Decimal(n1) / Decimal(d2)).quantize(SIXPLACES):
							print (str(n) + "/" + str(d) + " ==> " + str(Decimal(n) / Decimal(d)) + " = " + str(Decimal(n1) / Decimal(d2)))
