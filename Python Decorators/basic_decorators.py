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


#*args and **kwargs
'''Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

Example
Secure the function with *args and **kwargs arguments:'''

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("Aavi"))



#Decorator With Arguments
'''Decorators can accept their own arguments by adding another wrapper level.

Example
A decorator factory that takes an argument and transforms the casing based on the argument value.'''

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Aavi Bhardwaj"

print(myfunction())



