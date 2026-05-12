# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedAndHeight(root)[1]
    def isBalancedAndHeight(self, root) -> List:
        if root == None:
            return [0, True]

        left = self.isBalancedAndHeight(root.left)
        right = self.isBalancedAndHeight(root.right)

        return [1 + max(left[0], right[0]) , left[1] and right[1] and abs(left[0] - right[0]) <= 1]