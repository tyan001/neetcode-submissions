# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if self.dfs(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    
    def dfs(self, root, subRoot):

        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val == subRoot.val:
            bool1 = self.dfs(root.left, subRoot.left)
            bool2 = self.dfs(root.right, subRoot.right)
            return (bool1 and bool2)
        
        return False