numList = [10, 20, 30, 90.28, 100]

for i in range(1, 11):

	print("looping ... current index ... i:", i)

	if numList[i] == 90.28:

		print("found the number 90.28 at index i :", i) 
		print("breaking out of the loop")
		break
