# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    rootStack = []
    p = 0
    i = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if self.p >= len(preorder):
            return None
            
        root = TreeNode(preorder[self.p])
        self.rootStack.append(preorder[self.p])
        self.p += 1

        left = None
        right = None
        if len(self.rootStack) == 0 or inorder[self.i] != self.rootStack[-1]:
            left = self.buildTree(preorder, inorder)
        else:
            self.rootStack.pop()
            self.i += 1
        if len(self.rootStack) == 0 or inorder[self.i] != self.rootStack[-1]:
            right = self.buildTree(preorder, inorder)
        else:
            self.rootStack.pop()
            self.i += 1

        root.left = left
        root.right = right
        return root