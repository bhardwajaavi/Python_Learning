#Preserving Function Metadata
'''Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.'''



import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)