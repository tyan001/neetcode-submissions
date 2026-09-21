# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        is_valid = self.dfs(root, float("-inf"), float("inf"))
        
        return is_valid
        

    def dfs(self, root, left_bound, right_bound):
        if not root:
            return True

        if not (left_bound < root.val < right_bound):
            return False
        
        is_valid1 = self.dfs(root.left, left_bound, root.val)
        is_valid2 = self.dfs(root.right, root.val, right_bound)

        return is_valid1 and is_valid2



        

        