# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.heightAndDiameter(root)[1]
    def heightAndDiameter(self, root) -> List:
        if root == None:
            return [-1, 0]
        left = self.heightAndDiameter(root.left)
        right = self.heightAndDiameter(root.right)
        return [1 + max(left[0], right[0]), max(left[1], right[1], 2 + left[0] + right[0])]