# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced, _ = self.dfs(root)

        return balanced
    


    def dfs(self, node):


        if node is None:
            return [True,0]
        

        left= self.dfs(node.left)
        right = self.dfs(node.right)


        if not left[0] or not right[0]:
            balance = False
        elif abs(left[1] - right[1]) > 1:
            balance = False
        else:
            balance = True

        return [balance, 1+max(left[1], right[1])]

