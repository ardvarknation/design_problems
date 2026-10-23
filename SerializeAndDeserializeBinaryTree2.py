# Solution 2 for Leetcode Design problem "Serialize and Deserialize Binary Tree" 
# using Iterative BFS traversal approach.

# Description: 
#  Design an algorithm to serialize and deserialize a binary tree.
#  There is no restriction placed on how the serialization/deserialization 
#  algorithm should work. Just ensure that the binary tree can be serialized
#  to a string and this string can be deserialized into original tree structure.

# Constraints:
# - The number of nodes in the tree is in the range [0, 10^4]
# - -1000 <= Node.val <= 1000

# Complexity: 
# - Time: O(n) for Serialize/Deserialize operations
# - Space: O(n) for Serialize/Deserialize operations

# Definition for a binary tree node.
# class TreeNode(object):
#  def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None

# Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

from collections import deque

class Codec():

  def serialize(self, root):
    """
    Encodes a binary tree to a single string using BFS.

    @type root: TreeNode
    @rtype: str
    """

    if not root:
      return "#"

    result = []
    queue = deque([root])

    while queue:
      node = queue.popleft()

      if node is None:
        # Store null children explicitly.
        result.append("#")
      else:
        # Store current node value.
        result.append(str(node.val))

        # Add children even if they are None.
        queue.append(node.left)
        queue.append(node.right)

    return ",".join(result)

  def deserialize(self, data):
    """
    Decodes serialized string back into a tree.

    @type root: str
    @rtype: TreeNode
    """

    if data == "#":
      return None

    values = data.split(",")

    # First value is always the root.
    root = TreeNode(int(values[0]))

    queue = deque([root])

    # Index points to the next child value.
    i = 1

    while queue:
      parent = queue.popleft()

      # Left child.
      if values[i] != "#":
        parent.left = TreeNode(int(values[i]))
        queue.append(parent.left)
      i += 1

      # Right child.
      if values[i] != "#":
        parent.right = TreeNode(int(values[i]))
        queue.append(parent.right)
      i += 1

    return root
      
