# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        result = []
        node_stack = [root]

        while node_stack:
            node = node_stack.pop()
            result.append(node.val)
            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)
        
        return result