# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if root is []:
            return []

        self.inorder(root, res, k)

        return res[k-1]

    def inorder(self,root,res,k):

        if root is None or k == 0:
            return
        
        
        self.inorder(root.left,res,k)
        res.append(root.val)
        self.inorder(root.right, res, k)