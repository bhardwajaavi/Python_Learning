''' Stack is a linear data structure which works on Last in First out Principle(LIFO)'''

#for example we have stack of sandwiches so we can remove from the bottom means the last one will remove first.

'''     A stack is a data structure which can hold many elements and remove the last element from the top at the first'''

"""Basics Operations we can do on stacks:
1.Push- to add an element
2.Pop- to remove and return the element to the top
3.Peek- returns the top(last) element at the stack
4.isempty- check whether the stack is empty 
5.Size- Find the number of elements in the stack.

Stacks can be Implemented using arrays or linked lists.

Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.




"""



#Stack Implementation using Python Lists

stack=[]
stack.append(1)
stack.append(2)                         #push
stack.append(3)
print(stack)



topelement=stack[-1]                    #peek
print(topelement)



poppedelement=stack.pop()
print(poppedelement)                    #pop
print(stack)
stack.pop()
print(stack)



isempty=not bool(stack)
print(isempty)                          #isempty



print("size",len(stack))

