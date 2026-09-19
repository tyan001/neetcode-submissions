# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.dfs(root)

        return root

    
    def dfs(self,node):

        if node is None:
            return 

        node.right , node.left = node.left, node.right

        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)