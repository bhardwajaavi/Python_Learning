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
  
  
  #Else in For Loop
'''The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

Example
Print all numbers from 0 to 5, and print a message when the loop has ended:'''

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  
  #Nested Loops
'''A nested loop is a loop inside a loop.'''

'''The "inner loop" will be executed one time for each iteration of the "outer loop":

Example
Print each adjective for every fruit:'''

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
    
    #The pass Statement
'''for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

Example'''

for x in [0, 1, 2]:
  pass