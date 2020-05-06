def collatzCount(n):
    count = 0
    while n > 1:
        count = count + 1
        n = n / 2 if n % 2 == 0 else 3 * n + 1
    return count

max = -1
maxN = -1
for n in range(2, 1000000):
    cnt = collatzCount(n)
    if cnt > max:
        max = cnt
        maxN = n
print ("max = " + str(max) + " occurs for maxN = " + str(maxN))
