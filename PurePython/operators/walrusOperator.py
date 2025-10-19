"""
Introduced in Python 3.8, 
the walrus operator (:=) lets you assign 
a value to a variable inside an expression — 
instead of doing it on a separate line.
"""

data = input("Enter text: ")
if len(data) > 5:
    print("Long input!")

print("\n")

# example use of walrus operator
print(n := "="*20)


if (n := len(input("Enter text: "))) > 5:
    print(f"Long input! ({n} characters)")
