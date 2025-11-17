#A linked list consists of nodes with some sort of data, and a pointer, or link, to the next node.

'''Linked Lists vs Arrays
The easiest way to understand linked lists is perhaps by comparing linked lists with arrays.
Linked lists consist of nodes, and is a linear data structure we make ourselves, unlike arrays which is an existing data structure in the programming language that we can use.
Nodes in a linked list store links to other nodes, but array elements do not need to store links to other elements.

'''

'''The table below compares linked lists with arrays to give a better understanding of what linked lists are.

Arrays	Linked Lists
An existing data structure in the programming language	Yes	No
Fixed size in memory	Yes	No
Elements, or nodes, are stored right after each other in memory (contiguously)	Yes	No
Memory usage is low
(each node only contains data, no links to other nodes)	Yes	No
Elements, or nodes, can be accessed directly (random access)	Yes	No
Elements, or nodes, can be inserted or deleted in constant time, no shifting operations in memory needed.	No	Yes'''



'''These are some key linked list properties, compared to arrays:

Linked lists are not allocated to a fixed size in memory like arrays are, so linked lists do not require to move the whole list into a larger memory space when the fixed memory space fills up, like arrays must.
Linked list nodes are not laid out one right after the other in memory (contiguously), so linked list nodes do not have to be shifted up or down in memory when nodes are inserted or deleted.
Linked list nodes require more memory to store one or more links to other nodes. Array elements do not require that much memory, because array elements do not contain links to other elements.
Linked list operations are usually harder to program and require more lines than similar array operations, because programming languages have better built in support for arrays.
We must traverse a linked list to find a node at a specific position, but with arrays we can access an element directly by writing myArray[5].
'''


'''Types of Linked Lists
There are three basic forms of linked lists:

Singly linked lists
Doubly linked lists
Circular linked lists
'''