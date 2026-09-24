# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def __init__(self):
    #     self.count = 0

    # def goodNodes(self, root: TreeNode) -> int:
    #     self.dfs(root, -101)
    #     return self.count
    
    # def dfs(self, root, current_max):

    #     if root is None:
    #         return 
       
    #     if current_max <= root.val:
    #         self.count+=1
    #         current_max = root.val
        
    #     self.dfs(root.left, current_max)
    #     self.dfs(root.right, current_max)


    #     def goodNodes(self, root: TreeNode) -> int:
    #     self.dfs(root, -101)
    #     return self.count

    def goodNodes(self, root: TreeNode) -> int:

        return self.dfs(root, -101, 0)

    def dfs(self, root, current_max, count):

        if root is None:
            return count
       
        if current_max <= root.val:
            count+=1
            current_max = root.val
        
        count = self.dfs(root.left, current_max, count)
        count = self.dfs(root.right, current_max, count)
        return count
        





        
