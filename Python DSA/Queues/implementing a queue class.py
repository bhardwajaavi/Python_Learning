#mplementing a Queue Class

class queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
        if self.isempty():
            return"queue is empty"
        return self.queue.pop(0)
    def peek(self):
        if self.isempty():
            return"queue is empty"
        return self.queue[0]
    def isempty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)

#create a queue
myqueue=queue()

myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)
myqueue.enqueue(6)

print("queue is:",myqueue.queue)
print("Dequeue is:",myqueue.dequeue())
print("peek:",myqueue.peek())
print("again queue after popped:",myqueue.queue)
print("isempty:",myqueue.isempty())
print("size:",myqueue.size())
    
        