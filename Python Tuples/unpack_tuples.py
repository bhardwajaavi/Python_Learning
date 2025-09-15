#Unpacking a Tuple
'''When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
ExampleGet your own Python Server
Packing a tuple:'''

fruits = ("apple", "banana", "cherry")

#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Using Asterisk*
'''If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":'''

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)