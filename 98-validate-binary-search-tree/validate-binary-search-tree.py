# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def dfs(r, minv, maxv):
            if not r:
                return True
            
            left = dfs(r.left, minv, r.val)
            right = dfs(r.right, r.val, maxv)

            if r.val <= minv or r.val >= maxv:
                return False
            return left and right
        
        return dfs(root, float('-inf'), float('inf'))
            
        