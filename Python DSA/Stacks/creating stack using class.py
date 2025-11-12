'''While Python lists can be used as stacks, creating a dedicated Stack class provides better encapsulation and additional functionality:'''

#Creating a stack using class:

class stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isempty():
            return"Stack is Empty"
        return self.stack.pop()
    def peek(self):
        if self.isempty():
            return"Stack is empty"
        return self.stack[-1]
    def isempty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    
    
#creating a stack
mystack=stack()
    
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
    
print("Stack:",mystack.stack)
print("pop:", mystack.pop())
print("mystack after Pop:",mystack.stack)
print("peek:", mystack.peek())
print("mystack after Peek:",mystack.stack)
print("isempty:",mystack.isempty())
print("size:", mystack.size())
    