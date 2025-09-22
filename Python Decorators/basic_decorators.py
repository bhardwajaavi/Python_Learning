'''Decorators let you add extra behavior to a function, without changing the function's code.
A decorator is a function that takes another function as input and returns a new function.

'''


#Basic Decorator
'''A basic decorator that uppercases the return value of the decorated function.'''

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#Multiple Decorator Calls
'''A decorator can be called multiple times. Just place the decorator above the function you want to decorate.'''

#Example
'''Using the @changecase decorator on two functions:'''

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())


#Arguments in the Decorated Function
'''Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:'''
'''Functions with arguments can also be decorated:'''

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("Aavi"))



