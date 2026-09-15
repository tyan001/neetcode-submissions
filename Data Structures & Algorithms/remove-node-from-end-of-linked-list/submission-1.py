# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return head

        length = self.get_length(head)

        if length < n:
            return head
    
        if (length - n) == 0:

            return head.next


        curr = head
        counter = 0

        while curr and counter < (length-n)-1:
            curr = curr.next
            counter += 1

        curr.next = curr.next.next
        return head

        
    def get_length(self, head: Optional[ListNode]):

        curr = head
        counter = 0
        while curr:
            curr = curr.next
            counter +=1
        return counter
