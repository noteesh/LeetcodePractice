# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return True

        def checkSimilar(r, s):
            if not r and not s:
                return True
            if not r:
                return False
            if not s:
                return False
            
            left = checkSimilar(r.left, s.left)
            right = checkSimilar(r.right, s.right)

            if r.val != s.val or not left or not right:
                return False

            return True

        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        if root.val == subRoot.val and checkSimilar(root, subRoot):
            return True
        
        return l or r

