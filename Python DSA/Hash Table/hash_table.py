'''Hash Table
A Hash Table is a data structure designed to be fast to work with.
The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for, adding, and deleting data can be done really quickly, even for large amounts of data.
In a Linked List, finding a person "Bob" takes time because we would have to go from one node to the next, checking each node, until the node with "Bob" is found.
And finding "Bob" in an list/array could be fast if we knew the index, but when we only know the name "Bob", we need to compare each element and that takes time.
With a Hash Table however, finding "Bob" is done really fast because there is a way to go directly to where "Bob" is stored, using something called a hash function.
Building A Hash Table from Scratch
To get the idea of what a Hash Table is, let's try to build one from scratch, to store unique first names inside it.
We will build the Hash Table in 5 steps:
Create an empty list (it can also be a dictionary or a set).
Create a hash function.
Inserting an element using a hash function.
Looking up an element using a hash function.
Handling collisions.
'''
'''Step 1: Create an Empty List
To keep it simple, let's create a list with 10 empty elements.
'''
my_list = [None, None, None, None, None, None, None, None, None, None]
'''Each of these elements is called a bucket in a Hash Table.

Step 2: Create a Hash Function
Now comes the special way we interact with Hash Tables.
We want to store a name directly into its right place in the array, and this is where the hash function comes in.
A hash function can be made in many ways, it is up to the creator of the Hash Table. A common way is to find a way to convert the value into a number that equals one of the Hash Table's index numbers, in this case a number from 0 to 9.
In our example we will use the Unicode number of each character, summarize them and do a modulo 10 operation to get index numbers 0-9.
Example
Create a Hash Function that sums the Unicode numbers of each character and return a number between 0 and 9:
'''
def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))