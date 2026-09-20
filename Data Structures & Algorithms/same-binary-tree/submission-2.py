# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return self.dfs(p,q)
    
    def dfs(self, node1, node2):

        if node1 is None and node2 is None:
            return True

        if not node1:
            return False
        
        if not node2:
            return False
        

        if node1.val != node2.val:
            return False
        
        bool1 = self.dfs(node1.left, node2.left)
        bool2 = self.dfs(node1.right, node2.right)
        
        return bool1 and bool2
        

        