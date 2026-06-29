# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        good = 0
        maxStack = [[root, root.val]]
        while maxStack:
            maxNode = maxStack.pop()
            node = maxNode[0]
            if maxNode[1] <= node.val:
                good += 1
            if node.left:
                maxStack.append([node.left, max(node.left.val, maxNode[1])])
            if node.right:
                maxStack.append([node.right, max(node.right.val, maxNode[1])])
        return good