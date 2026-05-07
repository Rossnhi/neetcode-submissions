# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        def height(root):
            if root == None:
                return -1
            leftHeight = height(root.left)
            if leftHeight == -2:
                return -2
            rightHeight = height(root.right)
            if rightHeight == -2:
                return -2
            if abs(leftHeight - rightHeight) > 1:
                return -2
            return 1 + max(leftHeight, rightHeight)
        return False if height(root) == -2 else True