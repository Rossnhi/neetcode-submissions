# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.lowestCommonAncestorNone(root, p, q)
    def lowestCommonAncestorNone(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q) if root.left != None else None
            right = self.lowestCommonAncestor(root.right, p, q) if root.right != None else None
            if left != None:
                if right != None:
                    return root
                else:
                    return left
            if right != None:
                return right
            return None