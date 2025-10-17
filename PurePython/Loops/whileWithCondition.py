j = 0
numList = [10, 20, 70]

while (j <= len(numList) and numList[j] != 70 ):
	j += 2
	print("current j :", j)

print("stopped at j:", j)