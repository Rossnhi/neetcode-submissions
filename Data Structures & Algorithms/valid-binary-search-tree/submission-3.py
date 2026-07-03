# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTMinMax(root)[0]
        # if root == None:
        #     return True
        # else:
        #     left = True
        #     right = True
        #     if root.left:
        #         if root.left.val < root.val:
        #             left = self.isValidBST(root.left)
        #         else:
        #             return False
        #     if root.right:
        #         if root.right.val > root.val:
        #             right = self.isValidBST(root.right)
        #         else:
        #             return False
        #     return left and right
    
    def isValidBSTMinMax(self, root: Optional[TreeNode]) -> tuple[bool, int, int]:
        if root == None:
            return (True, 0, 0)
        left = (True, root.val, root.val)
        right = (True, root.val, root.val)
        if root.left:
            left = self.isValidBSTMinMax(root.left)
            if left[2] >= root.val:
                return (False, 0, 0)
        if root.right:
            right = self.isValidBSTMinMax(root.right)
            if right[1] <= root.val:
                return (False, 0, 0)
        return (left[0] and right[0], left[1], right[2])