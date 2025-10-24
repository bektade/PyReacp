"""

Materialize Iterators :

  - materialize => bring out conent to view or use

  - means getting a list or tuple from iterator object
  - use list() or tuple() constructor function to materialize
  - dict() can't be used to materialize!!

  - YOU CAN MATERIALIZE ONLY ONCE! or else need to re-create it!

"""


L = [1, 2, "A", "Z"]

# create instance of iterable 
it = iter(L)

# materialzie twice
t = tuple(it)
l = list(it)

# l is empty because we materialzied already
print(t, l)


it = iter(L)
t = tuple(it)

it = iter(L)
l = list(it)

print(t, l)


# dict can't be used to materialze!!
# di = dict(it)   