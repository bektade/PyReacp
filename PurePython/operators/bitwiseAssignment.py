"""
BITWISE ASSIGNMENT OPERATORS

- performs bitwise operation 
- then performs assignment

"""



# left shift and assign  <<=

x = 5
x <<= 3
print(x)


# right shift and assign  >>=

x = 5
x >>= 3
print(x)


# ^= means "bitwise XOR and assign"

"""
x = 5 → 0101
3     → 0011
----------------
XOR →   0110 -> 6


"""

x = 5 
x = x ^ 3

print("x ^= ", x)


# |= means “bitwise OR and assign”

"""
x = 5 → 0101
3     → 0011
----------------
OR →    0111

"""


x = 5
x |= 3

print(x)



# &= means “bitwise AND and assign”

"""
x = 5 → 0101
3     → 0011
----------------
OR →    0001

"""

x = 5
x &= 3

print(x)


# **= means “EXP and assign”



x = 5
x **= 2     # x = x**2

print(x)







