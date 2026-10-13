# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        depth = self.dfs(root, 0)
        return depth

    def dfs(self, root, depth):
        if root is None:
            return depth

        depth +=1

        left_depth = self.dfs(root.left, depth)
        right_depth = self.dfs(root.right, depth)

        return max(left_depth, right_depth)
