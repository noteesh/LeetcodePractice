# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True

        def heights(node):
            if not node:
                return 0

            left = heights(node.left)
            right = heights(node.right)

            if abs(left - right) > 1:
                nonlocal balanced
                balanced = False

            return max(left, right) + 1

        heights(root)
        return balanced

            