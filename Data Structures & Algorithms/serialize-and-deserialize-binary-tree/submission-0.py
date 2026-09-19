# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ""
        res = []
        queue = deque([root])
        while queue:

            node = queue.popleft()

            if not node:
                res.append("null") 
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        if not data:
            return None
        strings = data.split(",")
        root = TreeNode(int(strings[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()

            if strings[i] != "null":
                node.left = TreeNode(int(strings[i]))
                queue.append(node.left)
            i += 1

            if strings[i] != "null":
                node.right = TreeNode(int(strings[i]))
                queue.append(node.right)
            i += 1

        return root
