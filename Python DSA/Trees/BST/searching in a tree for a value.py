'''Search for a Value in a BST
Searching for a value in a BST is very similar to how we found a value using Binary Search on an array.
For Binary Search to work, the array must be sorted already, and searching for a value in an array can then be done really fast.
Similarly, searching for a value in a BST can also be done really fast because of how the nodes are placed.
'''

#How it works:
'''Start at the root node.
If this is the value we are looking for, return.
If the value we are looking for is higher, continue searching in the right subtree.
If the value we are looking for is lower, continue searching in the left subtree.
If the subtree we want to search does not exist, depending on the programming language, return None, or NULL, or something similar, to indicate that the value is not inside the BST.'''


class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def search(node, target):
  if node is None:
    return None
  elif node.data == target:
    return node
  elif target < node.data:
    return search(node.left, target)
  else:
    return search(node.right, target)

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

# Search for a value
result = search(root, 2)
if result:
  print(f"Found the node with value: {result.data}")
else:
  print("Value not found in the BST.")
