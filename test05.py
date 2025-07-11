
newlist = ["banana", "cherry", "kiwi", "apple", "melon", "mango"]

newlist = [x if x != "cherry" else "orange" for x in newlist]

newlist.sort(reverse=True)

print(newlist)




# List Comprehensions to create a list of squares from a list of numbers
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x ** 2 for x in nums]

print(squares)

"""


# List Comprehensions to get even numbers from a list
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bigNumbers = [x for x in numbers if x % 2 == 0 ]

print(bigNumbers)

"""

# List Comprehensions to convert all strings in a list to uppercase
"""
fruits = ["apple", "banana", "cherry"]

uppercase_fruits = [x.upper() for x in fruits]

print(uppercase_fruits)

"""