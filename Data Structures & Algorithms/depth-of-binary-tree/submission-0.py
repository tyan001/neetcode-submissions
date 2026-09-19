# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        if root is None:
            return 0

        depth = self.dfs(root, depth)
        return depth
    
    def dfs(self, node, depth):


        if node is None:
            return depth

        depth+=1
        depth_left = self.dfs(node.left, depth)
        depth_right = self.dfs(node.right,depth)

        return max(depth_left, depth_right)