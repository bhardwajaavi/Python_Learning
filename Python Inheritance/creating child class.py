'''Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

'''
#Create a class named Student, which will inherit the properties and methods from the Person class:
'''class Student(Person):
  pass'''


#Use the Student class to create an object, and then execute the printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("aavi", "Bhardwaj")
x.printname()






'''Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.

'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Aavi", "Bhardwaj")
x.printname()
