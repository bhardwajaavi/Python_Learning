'''Delete Object Properties
You can delete properties on objects by using the del keyword:
'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def myfun(self):
        print("Hello I am writing this code and my name is " +self.name )
        
p1=person ("Aavi",25)
p2=person ("Aneesh",29)    

p1.myfun()
p2.myfun()
        
