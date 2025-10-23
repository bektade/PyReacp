"""

 FUNCTIONAL PROGRAMMING TOOLS!

 three useful built-in functions for lists: 

	filter()
	map()
	reduce()


"""



def f(x) : return x % 3 == 0 or x % 5 == 0

def cubeIT(x) : return x**3

def add(x, y) : return x + y


def reduce(ls) :
	res = 0
	for x in range(0, len(ls)):
		print(x, ls[x])
		
		res = res + ls[x]

		
	return res




#### FILTER!!!!!
# divisible by 3 or 5
rez = filter(	f, 
		range(1, 10) )

print("divizible by 3 or 5? :", list(rez))



##### MAP!!!!

rezMAP = map(   cubeIT, 
		range(1,5) )
print(list(rezMAP))



##### REDUCE!!!
lala = [10,11,13]
rezREDUCE = reduce(lala)
print("redue",rezREDUCE)

