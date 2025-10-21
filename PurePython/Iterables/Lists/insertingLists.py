"""
inserting using slice would replace multiple items of the slice by single item if only single Item given

banana and cherry are replaced by watermelon here!

"""


thislist = ["apple", "banana", "cherry", "mango"]
thislist[1:3] = ["watermelon"]
print(thislist)


"""
inserting using slice would replace multiple items of the slice by single item if only single Item given

banana and cherry are replaced by watermelon and nana

"""


thislist = ["apple", "banana", "cherry", "mango", "Kiwi"]
thislist[1:3] = ["watermelon", "nana"]
print(thislist)


"""
To insert a new list item, without replacing any of the existing values, 
we can use the insert() method.

The insert() method inserts an item at the specified index: and moves the next item further!

"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)