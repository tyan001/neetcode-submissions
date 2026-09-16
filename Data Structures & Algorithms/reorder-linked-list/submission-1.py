# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return 
        
        if head.next is None:
            return 

        dummy = ListNode(-1,head)

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        previous = None
        current = slow.next
        slow.next = None 

        while current:
            temp_node = current.next
            current.next = previous
            previous = current
            current = temp_node

        current = head
        while previous:
            next_current = current.next
            next_previous = previous.next
            
            current.next = previous
            previous.next = next_current

            previous = next_previous
            current = next_current
        
        
            
        
