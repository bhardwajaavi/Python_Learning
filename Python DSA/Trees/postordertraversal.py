'''Post-order Traversal of Binary Trees
Post-order Traversal is a type of Depth First Search, where each node is visited in a certain order..
Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree, followed by a visit to the root node. It is used for deleting a tree, post-fix notation of an expression tree, etc.
What makes this traversal "post" is that visiting a node is done "after" the left and right child nodes are called recursively.
This is how the code for Post-order Traversal looks like:'''

class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def postordertraversal(node):
    if node is None:
        return
    postordertraversal(node.left)
    postordertraversal(node.right) 
    print(node.data, end=",")
    
root=treenode('r')
nodeA=treenode('a')     
nodeB=treenode('b')
nodeC=treenode('c')
nodeD=treenode('d')  
nodeE=treenode('e')  
nodeF=treenode('f')  
nodeG=treenode('g')    

root.left=nodeA
root.right=nodeB

nodeA.left=nodeC
nodeA.right=nodeD

nodeB.left=nodeE
nodeB.right=nodeG

nodeF.left=nodeG
#traverse
postordertraversal(root)