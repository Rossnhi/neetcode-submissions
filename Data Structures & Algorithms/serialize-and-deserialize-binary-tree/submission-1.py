# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append("#")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        dataList = data.split(",")
        i = 1
        root = TreeNode(int(dataList[0]))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if dataList[i] != "#":
                left = TreeNode(int(dataList[i]))
                node.left = left
                queue.append(left)
            i += 1
            if dataList[i] != "#":
                right = TreeNode(int(dataList[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root
