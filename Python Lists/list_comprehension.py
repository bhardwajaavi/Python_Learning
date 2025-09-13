"""List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:"""
#Looping Using List Comprehension

'''List Comprehension offers the shortest syntax for looping through lists:
Example
A short hand for loop that will print all items in a list:'''



thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)



#The Syntax
'''newlist = [expression for item in iterable if condition == True]'''

'''The return value is a new list, leaving the old list unchanged.'''



#Iterable
'''The iterable can be any iterable object, like a list, tuple, set etc.

Example
You can use the range() function to create an iterable:'''




#Expression
'''The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

Example
Set the values in the new list to upper case:'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)



