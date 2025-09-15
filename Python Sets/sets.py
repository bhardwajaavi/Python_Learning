'''Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.

'''

set1 = {"apple", "banana", "cherry"}
print(set1)


#Duplicates Not Allowed
'''Sets cannot have two items with the same value.'''
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Get the Length of a Set
'''To determine how many items a set has, use the len() function.'''

'''Example
Get the number of items in a set:'''

thisset = {"apple", "banana", "cherry"}

print(len(thisset))



'''type()
From Python's perspective, sets are defined as objects with the data type 'set':

<class 'set'>
Example
What is the data type of a set?'''

myset = {"apple", "banana", "cherry"}
print(type(myset))


'''The set() Constructor
It is also possible to use the set() constructor to make a set.

Example
Using the set() constructor to make a set:'''

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#Python Collections (Arrays)
'''There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.'''
