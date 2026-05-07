# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def height(root):
            nonlocal res
            if root == None:
                return -1
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if abs(leftHeight - rightHeight) > 1:
                res = False
            return 1 + max(leftHeight, rightHeight)
        height(root)
        return res