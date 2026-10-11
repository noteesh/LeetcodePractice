# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        q = deque()
        ret = []
        q.append(root)
        if not root:
            return []

        while q:
            for i in range(len(q) - 1):
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            t = q.popleft()
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            ret.append(t.val)
        return ret