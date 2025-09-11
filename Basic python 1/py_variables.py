#Python Variables
"""In Python, variables are created when you assign a value to it:"""

x=5
y="hello,AAVI"
print(y)




#Assign Multiple values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables

x=y=z="orange"
print(x)
print(y)
print(z)

#Unpack a Collection
"""If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking."""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variables
"""Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside."""
 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)




#The global Keyword
"""Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword."""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#when one global variable is define outside function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)