#Since Python lists has good support for functionality needed to implement queues, we start with creating a queue and do queue operations with just a few lines:

#Using a Python list as a queue:

queue=[]

#Enqueue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

#Dequeue
poppedelement=queue.pop(2)
print("dequeue Element:", poppedelement)


print("after popped:", queue)

#peek
frontelement=queue[0]
print("Peek:",frontelement)

#isempty
isempty=not bool(queue)
print("isempty:",isempty)

#size
print("size:",len(queue))


'''Note: While using a list is simple, removing elements from the beginning (dequeue operation) requires shifting all remaining elements, making it less efficient for large queues.

'''