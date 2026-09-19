# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.longest_diameter = 0


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.dfs(root)
        return self.longest_diameter
        
    


    def dfs(self,node):

        if node is None:
            return 0


        left_length = self.dfs(node.left)
        right_length = self.dfs(node.right)
        self.longest_diameter = max(self.longest_diameter, left_length + right_length)

        return max(left_length,right_length) +1

