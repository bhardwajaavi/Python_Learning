'''he __str__() Method
The __str__() method controls what should be returned when the class object is represented as a string.
If the __str__() method is not set, the string representation of the object is returned:'''

#without using string method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)





#using string method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)