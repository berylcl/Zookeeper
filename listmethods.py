numbers = [2, 4,4, 5, 5, 78, 8, 90]
numbers.append(20)
numbers.insert(0, 423)
print(numbers)
for item in numbers:
    if item == item:
        numbers.remove(item)
        print(item)
#The index() method returns the index of the given element in the list.
# If the element is not found, a ValueError exception is raise
#The count() method returns the number of elements with the specified value
#The Python copy() method creates a copy of an existing list. The copy() method is added to the end of a list object
# and so it does not accept any parameters. copy() returns a new list.