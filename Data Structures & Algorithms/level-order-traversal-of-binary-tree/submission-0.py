# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        if root is None:
            return levels

        q = deque([root])


        while q:

            q_size = len(q)
            current_val = []
            
            for _ in range(q_size):
                node = q.popleft()
                current_val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            levels.append(current_val)
        
        return levels


            


        
