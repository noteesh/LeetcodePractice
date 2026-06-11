# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # depth-first search solution - preorder
        st = []
        st.append(root)

        while st:
            temp = st.pop()
            try:
                temp.left, temp.right = temp.right, temp.left
            except AttributeError:
                continue
            print(temp.left)
            print(temp.right)
            st.append(temp.right)
            st.append(temp.left)
        
        return root

