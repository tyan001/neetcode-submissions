# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return None
        
        if head.next is None:
            return head
        
        length = self.get_length(head)
        segments = length//k

        dummy = previous = ListNode(-1,head)
        start = dummy.next
        for i in range(segments):
            
            end = self.get_pos(start,k)     
            reverse_segment = self.reverse(start,end)
            previous.next = reverse_segment
            previous = start

            start = start.next

        return dummy.next


    def get_pos(self, node:ListNode, pos:int):

        current = node

        for _ in range(1,pos):
            current = current.next
        
        return current


    def get_length(self, head:ListNode) -> int:

        l = 0
        current = head

        while current:
            current = current.next
            l+=1
        
        return l
    

    def reverse(self, start:ListNode, end:ListNode):
        
        current = start
        right_bound = end.next
        previous = right_bound

        while current != right_bound:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous




        