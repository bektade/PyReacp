"""

bitwise operators are:

&  : 	AND

|  : 	OR

^  : 	XOR - Sets each bit to 1 if only one of two bits is 1

~  : 	NOT - INVERTS bits (~x = -(x + 1))

<< : 	Zero fill left shift - Shift left by pushing zeros in from the right and 
	let the leftmost bits fall off - MAKES THE NUMBER BIGGER

>> : 	Signed right shift - Shift right by pushing copies of the leftmost bit in from the left
     	and let the rightmost bits fall off	x

"""

print("~6", ~6)
# ~6  ==  -(6 + 1)  ==  -7




print("6 AND 3:",6 & 3)

# 6 	is 0110
# 3 	is 0011
# 6 & 3 is 0010 => 2


print("6 OR 3:",6 | 3)



print("6 XOR 3 is 101: ", 6^3)
print("3 XOR 6 is 101: ", 3^6)



x = 6        # binary: 0000 0110
y = x << 2   # shift left by 2 bits → 0001 1000


print("6 << 2", y)     # 24

x = 6        # binary: 0000 0110
y = x >> 2   # shift RIGHT by 2 bits → 0000 0001

print("6 >> 2",y)     # 1



"""
NOTE:

In Python bitwise operations never overflow BCZ integers have no fixed bit length in Python they can grow arbitrarily large.

In C or PLCs, numbers have fixed bit widths (e.g., 8-, 16-, or 32-bit), meaning shifts and bitwise operations are limited to that size and can overflow or lose bits beyond their boundary.

"""


