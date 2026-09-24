# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        return self.dfs(root, 0, -101)
    
    def dfs(self, root,count, current_max):

        if root is None:
            return count
        good = 0
        if current_max <= root.val:
            good = 1
            current_max = root.val
        
        left_count = self.dfs(root.left, count, current_max)
        right_count = self.dfs(root.right,count, current_max)

        return good + left_count + right_count





        
