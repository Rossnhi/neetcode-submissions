# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if root == None:
            return res
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res += "#" + str(node.val)
            else:
                res += "#" + str(node)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        nodes = []
        if data == "":
            return None
        i = 1
        j = 0
        level = []
        while i < len(data):
            val = ""
            while i < len(data) and data[i] != "#":
                val += data[i]
                i += 1
            if len(nodes) == 0:
                nodes.append([TreeNode(int(val))])
                i += 1
                continue
            node = TreeNode(int(val)) if val != "None" else None
            if j % 2 == 0:
                nodes[-1][j//2].left = node
            else:
                nodes[-1][j//2].right = node
            if node:
                level.append(node)
            j += 1
            if j/2 == len(nodes[-1]):
                nodes.append(level)
                level = []
                j = 0
            i += 1
        return nodes[0][0]