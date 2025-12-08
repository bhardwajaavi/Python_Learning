'''Find The Lowest Value in a BST Subtree
The next section will explain how we can delete a node in a BST, but to do that we need a function that finds the lowest value in a node's subtree.

How it works:

Start at the root node of the subtree.
Go left as far as possible.
The node you end up in is the node with the lowest value in that BST subtree.
This is how a function for finding the lowest value in the subtree of a BST node looks like:

Example
Find the lowest value in a BST subtree'''

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

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

# Traverse
inOrderTraversal(root)

# Find Lowest
print("\nLowest value:",minValueNode(root).data)
'''hfhjzjfdlir'''