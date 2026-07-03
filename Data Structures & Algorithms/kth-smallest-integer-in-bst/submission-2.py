# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        val = 0
        def inOrder(root) :
            nonlocal i
            nonlocal val
            if i >= k :
                return
            if root:
                inOrder(root.left)
                i += 1
                if i == k:
                    val = root.val
                    return
                inOrder(root.right)
            return
        inOrder(root)
        return val