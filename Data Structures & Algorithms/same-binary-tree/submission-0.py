# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queueP = deque([p])
        queueQ = deque([q])
        
        while queueP or queueQ:
            nodep = queueP.popleft()
            nodeq = queueQ.popleft()

            if nodep is None and nodeq is None:
                continue
            if nodep is None or nodeq is None or nodep.val != nodeq.val:
                return False

            queueP.append(nodep.left)
            queueP.append(nodep.right)
            queueQ.append(nodeq.left)
            queueQ.append(nodeq.right)

        return True
            


        