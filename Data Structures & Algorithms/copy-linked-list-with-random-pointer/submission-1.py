"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        nodeHash = {}

        current = head

        while current:
            node = Node(current.val)
            nodeHash[current] = node
            current = current.next
        
        current = head

        while current:
            node = nodeHash[current]
            if current.next is None:
                node.next = None
            else:
                node.next = nodeHash[current.next]

            if current.random is None:
                node.random = None
            else:
                node.random = nodeHash[current.random]
            current = current.next
        
        return nodeHash[head]


        
        