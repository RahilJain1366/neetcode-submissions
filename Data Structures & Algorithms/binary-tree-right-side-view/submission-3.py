# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = []

        if not root:
            return levels
        def dfs(node, level):
            
            nonlocal levels

            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)

            if node.left:
                dfs(node.left, level + 1)
            
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        res = []
        for level in levels:
            res.append(level[-1])

        return res