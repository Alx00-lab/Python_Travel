thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

newlist = []
# Using a for loop to create a new list with items that contain the letter "a"

"""
for x in thislist:
    if "a" in x:
        newlist.append(x)

print(newlist)
"""
# Using list comprehension to achieve the same result
newlist = [x for x in thislist if "a" in x]

print(newlist)