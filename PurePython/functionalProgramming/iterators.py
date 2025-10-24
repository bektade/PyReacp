"""

Iterator:

- is an object representing a stream of data
- this object RETURNS the data ONE ELEMENT at a time. 
- iterator supports __next__() method!
- iterators could be finitie or infinite.

- iterators support iteration 
	- built in data types e.g. lists & dicts



"""


# example 

L = [1, 2, "A"]

it = iter(L)   # create an instance of terator


print("type of obj it:", type(it), it)

"""
print(it.__next__())
print(it.__next__())
print(it.__next__())
"""

# another way
print(next(it))
print(next(it))
print(next(it))