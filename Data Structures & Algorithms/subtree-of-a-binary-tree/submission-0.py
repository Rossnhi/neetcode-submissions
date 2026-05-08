# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return subRoot == None
        queue = deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            if self.isSame(node, subRoot):
                return True
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return False
    def isSame(self, p, q) -> bool:
        if p == None or q == None:
            return p == None and q == None
        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)