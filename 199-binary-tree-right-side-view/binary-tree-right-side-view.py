# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        ret = []
        queue.append(root)

        while queue:
            level = []
            for n in range(len(queue)):
                temp = queue.popleft()
                if not temp:
                    continue
                level.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            ret.append(level[-1])
        
        return ret
            