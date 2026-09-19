# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #Depth First Search method

        def dfs(root):

            if not root: return [True, 0]

            leftsub, rightsub = dfs(root.left), dfs(root.right)

            balanced = leftsub[0] and rightsub[0] and abs(leftsub[1] - rightsub[1]) <= 1

            return [balanced, 1 + max(leftsub[1],rightsub[1])]

        return dfs(root)[0]

            
