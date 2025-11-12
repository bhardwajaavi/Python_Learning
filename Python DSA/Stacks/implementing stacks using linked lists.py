'''A linked list consists of nodes with some sort of data, and a pointer to the next node.

A singly linked list.
A big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.'''


#Creating a Stack using a Linked List:
class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,value):
        newnode=node(value)
        if self.head:
            newnode.next=self.head
        self.head=newnode
        self.size+=1
    def pop(self):
        if self.isempty():
            return"stack is empty"
        poppednode=self.head
        self.head=self.head.next
        self.size-=1
        return poppednode.value
    def peek(self):
        if self.isempty():
            return"stack is empty"
        return self.head.value
    def isempty(self):
        return self.size==0
    def stacksize(self):
        return self.size
    def traverseandprint(self):
        currentnode=self.head
        while currentnode:
            print(currentnode.value, end= " -> ")
            currentnode=currentnode.next
        print()
        
mystack=stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)

print("Linked list:",end="")
mystack.traverseandprint()
print("peek:",mystack.peek())
print("pop:",mystack.pop())
print("linked list after pop:",end="")
mystack.traverseandprint()
print("isempty:",mystack.isempty())
print("size:",mystack.stacksize())

        