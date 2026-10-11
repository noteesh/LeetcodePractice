# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        b = True

        def height(node):
            if not node:
                return 0
            nonlocal b
            if b is False:
                return 0
            
            l = height(node.left)
            r = height(node.right)

            if abs(l - r) > 1:
                b = False
            return max(l, r) + 1
        
        height(root)
        return b