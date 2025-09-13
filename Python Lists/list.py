#List
'''Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:'''

names = ["Aavi", "Satish", "Anita", "Aneesh"]
print(names)

#List Length
'''To determine how many items a list has, use the len() function:
Example
Print the number of items in the list:'''

names = ["Aavi", "Satish", "Anita", "Aneesh"]
print(len(names))



#List Items - Data Types
'''List items can be of any data type:'''

list1 = ["abc", 34, True, 40, "male"]
print(list1)


#type()
'''From Python's perspective, lists are defined as objects with the data type 'list':

<class 'list'>
Example
What is the data type of a list?'''

mylist = ["apple", "banana", "cherry"]
print(type(mylist))



#The list() Constructor
'''It is also possible to use the list() constructor when creating a new list.
Example
Using the list() constructor to make a List:'''

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
