#Change Item Value
'''To change the value of a specific item, refer to the index number:
Change the second item:'''

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)



#Change a Range of Item Values
'''To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)



#nsert Items
'''To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
Example
Insert "watermelon" as the third item:'''

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)