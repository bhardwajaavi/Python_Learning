#The __init__() Method
'''The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() method.
All classes have a method called __init__(), which is always executed when the class is being initiated.
Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created:'''

'''Example
Create a class named Person, use the __init__() method to assign values for name and age:'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
