"""
To find the diameter of a binary tree in Python, you can use a depth-first search (DFS) approach. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. You can calculate the diameter by finding the maximum of the following three values:

The diameter of the left subtree (recursively).
The diameter of the right subtree (recursively).
The longest path that goes through the root node, which is the height of the left subtree plus the height of the right subtree.
Here's a Python program to find the diameter of a binary tree:
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # Update the diameter if necessary
            self.diameter = max(self.diameter, left_height + right_height)
            # Return the height of the current node
            return 1 + max(left_height, right_height)

        self.diameter = 0
        height(root)
        return self.diameter

# Example usage:
# Construct a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
print("Diameter of the binary tree:", solution.diameterOfBinaryTree(root))
