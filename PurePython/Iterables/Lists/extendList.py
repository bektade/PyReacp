"""


Extend () : 

To append elements from another list to the current list
Works with any iterable!


We could also add them! ( works only iterables are the same)

"""


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)



thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "mama")
thislist.extend(thistuple)
print(thislist)





ls1 = ("A", "B")

ls2 = (3, "D")

ls3 = ls1 + ls2

print(ls3)