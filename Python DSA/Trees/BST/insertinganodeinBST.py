#Insert a Node in a BST
'''Inserting a node in a BST is similar to searching for a value.

How it works:

Start at the root node.
Compare each node:
Is the value lower? Go left.
Is the value higher? Go right.
Continue to compare nodes with the new value until there is no right or left to compare with. That is where the new node is inserted.'''


class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(node, data):
  if node is None:
    return TreeNode(data)
  else:
    if data < node.data:
      node.left = insert(node.left, data)
    elif data > node.data:
      node.right = insert(node.right, data)
    return node

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left) 
  print(node.data, end=", ")
  inOrderTraversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Inserting new value into the BST
insert(root, 2)

# Traverse
inOrderTraversal(root)
