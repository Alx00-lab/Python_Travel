#Sort the list based on how close the number is to 50

def myfunc(n): 
    return abs(n - 50)

numbers = [100, 50, 65, 82, 23]
numbers.sort(key = myfunc)
print(numbers)