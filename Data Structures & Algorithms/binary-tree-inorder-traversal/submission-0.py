# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # Root Left Right

        if root is None:
            return []

        result = []
        node_stack = []
        current = root
        while current or node_stack:

            while current:
                node_stack.append(current)
                current = current.left
            
            current = node_stack.pop()
            result.append(current.val)
            current = current.right

        return result
            

        