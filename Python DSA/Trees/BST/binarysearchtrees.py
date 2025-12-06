'''A Binary Search Tree is a Binary Tree where every node's left child has a lower value, and every node's right child has a higher value.
A clear advantage with Binary Search Trees is that operations like search, delete, and insert are fast and done without having to shift values in memory.'''


#Binary Search Trees
'''A Binary Search Tree (BST) is a type of Binary Tree data structure, where the following properties must be true for any node "X" in the tree:
The X node's left child and all of its descendants (children, children's children, and so on) have lower values than X's value.
The right child, and all its descendants have higher values than X's value.
Left and right subtrees must also be Binary Search Trees.
These properties makes it faster to search, add and delete values than a regular binary tree.
To make this as easy to understand and implement as possible, let's also assume that all values in a Binary Search Tree are unique.
The size of a tree is the number of nodes in it (n).
A subtree starts with one of the nodes in the tree as a local root, and consists of that node and all its descendants.
The descendants of a node are all the child nodes of that node, and all their child nodes, and so on. Just start with a node, and the descendants will be all nodes that are connected below that node.
The node's height is the maximum number of edges between that node and a leaf nod
A node's in-order successor is the node that comes after it if we were to do in-order traversal. In-order traversal of the BST above would result in node 13 coming before node 14, and so the successor of node 13 is node 14.

'''