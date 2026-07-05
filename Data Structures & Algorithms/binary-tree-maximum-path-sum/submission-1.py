# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -1000
        self.maxPathSumHelper(root)
        return self.max

    def maxPathSumHelper(self, root: Optional[TreeNode]) -> tuple[int, int, int]: # through both, ends at root from left, ends at root from right
        if root == None:
            return (0, 0, 0)
        print(root.val)
        left = (0, 0, 0)
        right = (0, 0, 0)
        if root.left:
            left = self.maxPathSumHelper(root.left)
        if root.right:
            right = self.maxPathSumHelper(root.right)
        res = (max(left[1], left[2]) + root.val + max(right[1], right[2]), max(left[1], left[2]) + root.val, root.val + max(right[1], right[2]))
        res = (max(root.val, res[0]), max(root.val, res[1]), max(root.val, res[2]))
        self.max = max(self.max, res[0], res[1], res[2])
        print(left, right, res)
        return res