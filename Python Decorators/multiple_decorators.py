#Multiple Decorators
'''You can use multiple decorators on one function.
This is done by placing the decorator calls on top of each other.
The decorators are called in the order they are specified.
Example
One decorator for upper case, and one for adding a greeting:'''

#Example
'''One decorator for upper case, and one for adding a greeting:'''

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Aavi Bhardwaj"

print(myfunction())