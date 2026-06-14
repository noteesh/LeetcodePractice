# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        1) if they are good
        2) count of good nodes
        3) if I am a good node or not
        '''

        if not root:
            return 0

        def good(node, maxSoFar):
            if not node:
                return 0
            
            left = good(node.left, max(maxSoFar, node.val))
            right = good(node.right, max(maxSoFar, node.val))

            if node.val >= maxSoFar:
                return 1 + left + right
        
            return left + right
        
        return good(root, float('-inf'))