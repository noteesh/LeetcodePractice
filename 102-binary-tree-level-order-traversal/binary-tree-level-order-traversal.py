# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        q = deque()
        ret = []
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                temp = q.popleft()
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            ret.append(level)
        
        return ret