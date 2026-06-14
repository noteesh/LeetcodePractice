# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isEqual(node, subNode):
            if not node and not subNode:
                return True
            if not subNode:
                return False
            if not node:
                return False

            
            left = isEqual(node.left, subNode.left)
            right = isEqual(node.right, subNode.right)

            if node.val != subNode.val or not left or not right:
                return False
            return True
        
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        if root.val == subRoot.val and isEqual(root, subRoot):
            return True

        return left or right


                