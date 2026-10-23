# Solution 1 for Leetcode Design problem "Serialize and Deserialize Binary Tree" 
# using DFS Preorder traversal approach.

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

class Codec():

  def serialize(self, root):
    """
    Encodes a binary tree to a single string.

    @type root:  TreeNode
    @rtype:  str
    """

    result = []

    def dfs(node):
      # Store null markers explicitly.
      if not node:
        result.append("#")
        return

        # Preorder: root -> left -> right
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return ",".join(result)

  def deserialize(self, data):
    """
    Decodes string data to a binary tree.

    @type data : str
    @rtype : TreeNode
    """

    values = iter(data.split(","))

    def dfs():
      val = next(values)

      # Null marker.
      if val == "#":
        return None

      # Create current node.
      node = TreeNode(int(val))

      # Reconstruct left subtree.
      node.left = dfs()

      # Reconstruct right subtree.
      node.right = dfs()

      return node

    return dfs()
