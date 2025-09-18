#Looping Through a String
'''Even strings are iterable objects, they contain a sequence of characters:

Example
Loop through the letters in the word "banana":'''

for x in "banana":
  print(x)
  
  
  #The break Statement
'''With the break statement we can stop the loop before it has looped through all the items:

Example
Exit the loop when x is "banana":'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#The continue Statement
'''With the continue statement we can stop the current iteration of the loop, and continue with the next:

Example
Do not print banana:'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  
  #The range() Function
'''To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Example
Using the range() function:'''

for x in range(6):
  print(x)
  
  
  