# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        numgood = 0

        def counting(r, maxSoFar):
            if not r:
                return
            
            left = counting(r.left, max(r.val, maxSoFar))
            right = counting(r.right, max(r.val, maxSoFar))

            if r.val >= maxSoFar:
                nonlocal numgood
                numgood += 1
        
        counting(root, float('-inf'))
        return numgood