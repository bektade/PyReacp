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

rezREDUCE = reduce(add, range(1, 11))
print(list(rezREDUCE))

