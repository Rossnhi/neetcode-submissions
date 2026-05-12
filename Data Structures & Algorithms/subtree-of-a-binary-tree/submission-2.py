# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return subRoot == None
        if subRoot == None:
            return True
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if self.isSame(node, subRoot):
                return True
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return False
    def isSame(self, p, q) -> bool:
        if p == None or q == None:
            return p == None and q == None
        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)