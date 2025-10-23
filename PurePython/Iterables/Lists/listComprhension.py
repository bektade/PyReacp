evenCombo = []

for x in [1, 2, 3]:
	for y in [3, 1, 4]:
		if (x + y) % 2 == 0 :
			evenCombo.append((x, y))


print("evnCombo: ", evenCombo)



"""
LIST COMPREHENSION :

- the rightmost condition is where the code 

"""

oddCombo = [ (x, y) for x in [1, 2, 3] for y in [3, 1,4 ] if (x+y) % 2 != 0]
print("oddCombo: ", oddCombo)


# flatten a list using a listcomp with two 'for'


vec = [[1,2,3], [4,5,6], [7,8,9]]

flat = [i for X in vec for i in X]
print(flat, "\n")



# approx pi

from math import pi

piLS = [ round(pi, i) for i in range(0, 6)]
print("piRound:", piLS)


