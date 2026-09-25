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

    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if root is [] or k < 0:
            return []
        
        stack = []
        current = root
        while stack or current:

            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            res.append(current.val)
            k -= 1
            if k==0:
                return res[-1]
            
            current = current.right
        



        