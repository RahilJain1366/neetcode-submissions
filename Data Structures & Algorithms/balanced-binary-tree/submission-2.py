# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #Brute Force Method
        result = []
        flag = 0
        if not root:
            return True

        leftsub = self.HeightBalance(root.left)
        rightsub = self.HeightBalance(root.right)
        print("Left Sub Tree: {} || Right Sub Tree: {}".format(leftsub,rightsub))
        difference = abs(leftsub - rightsub)
        print(difference)
        if difference <= 1:
            difference = 0
            nodeleft = self.isBalanced(root.left)
            noderight = self.isBalanced(root.right)
            result.append(nodeleft)
            result.append(noderight)
            print("node left {} || node right {} || result {}".format(nodeleft,noderight, result))
        else:
            return False
        if False in result:
            return False
        else:
            return True
    def HeightBalance(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return 1 + max(self.HeightBalance(root.left), self.HeightBalance(root.right))