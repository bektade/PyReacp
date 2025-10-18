"""

is : operator checks whether two variables refer to the same object in memory

== : checks whether their values are equal.


So, a is b means both names point to the same object, whereas a == b means their contents are the same, even if they’re different objects.

"""

a = [1, 2, 3]
b = [4, 5, 6]

print(a == b)  # True  (same value)
print(a is b)  # False (different objects)


a = b
print("a",a)
print("b",b)
print(a == b)  # True  (same value)
print(a is b)  # False (different objects)

