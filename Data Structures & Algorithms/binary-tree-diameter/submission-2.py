# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.depthAndDiameterOfBinaryTree(root)[1]
    def depthAndDiameterOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return [-1, 0] # -1 because deth in term of edges not nodes, if nodes then 0
        l = self.depthAndDiameterOfBinaryTree(root.left)
        r = self.depthAndDiameterOfBinaryTree(root.right)
        depth = 1 + max(l[0], r[0])
        return [
            depth,
            max(l[1], r[1], 2 + l[0] + r[0])
        ]