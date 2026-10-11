# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        same = True

        def st(pn, qn):
            if not pn and not qn:
                return
            nonlocal same
            if not pn:
                same = False
                return
            if not qn:
                same = False
                return
            
            st(pn.left, qn.left)
            st(pn.right, qn.right) 

            if pn.val != qn.val:
                same = False
                
            return pn, qn
        
        st(p, q)
        return same