# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = 0
        ret = 0

        def inorder(r):

            if not r:
                return None
            
            inorder(r.left)

            nonlocal count
            nonlocal ret
            if r:
                count += 1
                if count == k:
                    ret = r.val
            
            inorder(r.right)
        
            return r
        
        inorder(root)
        return ret
        