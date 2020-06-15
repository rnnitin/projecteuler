
prev = 1;
curr = 1;
currStr = str(curr);
index = 2;
while len(currStr) < 1000:
	tcurr = curr + prev;
	prev = curr;
	curr = tcurr;
	index = index + 1;
	currStr = str(curr);
	if index < 15:
		print (str(index) + " -> " + str(curr))
	if len(currStr) % 10 == 0:
		print ("len(currStr) = " + str(len(currStr)))
print (str(curr))
print ("index = " + str(index))
