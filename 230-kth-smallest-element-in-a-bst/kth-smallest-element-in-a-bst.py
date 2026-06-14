# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        desiredValue = -1
        count = 0

        def inorderDFS(node):
            if not node:
                return 
            
            inorderDFS(node.left)
            nonlocal desiredValue
            nonlocal count
            count += 1
            if count == k:
                desiredValue = node.val
            
            inorderDFS(node.right)

            return node

        inorderDFS(root)
        return desiredValue