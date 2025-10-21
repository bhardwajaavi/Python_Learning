#Create a Parent Class
'''Any class can be a parent class, so the syntax is the same as creating any other class:'''

#Create a class named Person, with firstname and lastname properties, and a printname method:

class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print(self.fname,self.lname)
    
x=person("aavi","bhardwaj")
x.printname()