# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        leftMaxDepth = self.MaxDepth(root.left)
        rightMaxDepth = self.MaxDepth(root.right)
        diameter = leftMaxDepth + rightMaxDepth

        sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

        return max (diameter,sub)


        
    def MaxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        return 1 + max(self.MaxDepth(root.left), self.MaxDepth(root.right))

        



       