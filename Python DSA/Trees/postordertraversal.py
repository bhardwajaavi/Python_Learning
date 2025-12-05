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