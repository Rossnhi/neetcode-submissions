from _heapq import heapify
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.heightAndIsBalanced(root)[1]
    def heightAndIsBalanced(self, root) -> List:
        if root == None:
            return [-1, True]

        left = self.heightAndIsBalanced(root.left)
        right = self.heightAndIsBalanced(root.right)

        if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
            return [1 + max(left[0], right[0]) , True]
        return [1 + left[0] + right[0] , False]