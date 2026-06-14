# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True

        def isSimilar(pNode, qNode):
            nonlocal same
            if not pNode and not qNode:
                return
            elif not pNode:
                same = False
                return
            elif not qNode:
                same = False
                return

            if pNode.val != qNode.val:
                same = False
            
            left = isSimilar(pNode.left, qNode.left)
            right = isSimilar(pNode.right, qNode.right)

            
            return pNode, qNode
        
        isSimilar(p, q)
        return same