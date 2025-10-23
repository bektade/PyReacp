thislist = ["apple", "banana", "cherry"]



for x in thislist:
	print(x)


for i in range(len(thislist)):
  print(thislist[i], i)



i = 1
while i < len(thislist):
  print(thislist[i], i)
  i = i + 1


# list comprehension

thislist = [1, 3, 5, 7, 11]


x = [x**2 for x in thislist]

print(x)