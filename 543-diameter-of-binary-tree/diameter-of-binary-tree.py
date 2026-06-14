# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return -1
            nonlocal diameter

            leftPath = longest_path(node.left)
            rightPath = longest_path(node.right)

            diameter = max(diameter, leftPath + rightPath + 2)

            return max(leftPath, rightPath) + 1
        
        longest_path(root)
        return diameter