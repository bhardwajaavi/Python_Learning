'''In-order Traversal of Binary Trees
In-order Traversal is a type of Depth First Search, where each node is visited in a certain order.
In-order Traversal does a recursive In-order Traversal of the left subtree, visits the root node, and finally, does a recursive In-order Traversal of the right subtree. This traversal is mainly used for Binary Search Trees where it returns values in ascending order.
What makes this traversal "in" order, is that the node is visited in between the recursive function calls. The node is visited after the In-order Traversal of the left subtree, and before the In-order Traversal of the right subtree.
This is how the code for In-order Traversal looks like:'''

class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def inordertraversal(node):
    if node is None:
        return    
    inordertraversal(node.left)
    print(node.data, end=",")  
    inordertraversal(node.right)

root=treenode('R')
nodeA=treenode('A')
nodeB=treenode('B')
nodeC=treenode('C')
nodeD=treenode('D')
nodeE=treenode('E')
nodeF=treenode('F')
nodeG=treenode('G')

root.left=nodeA
root.right=nodeB

nodeA.left=nodeC
nodeA.right=nodeD

nodeB.left=nodeE
nodeB.right=nodeG

nodeE.left=nodeF

#traverse
inordertraversal(root)

'''the is extra line made by aavi bhardwaj only
'''