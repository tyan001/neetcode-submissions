# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]

        mid = l + (r - l) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        return self.conquer(left, right)

    def conquer(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next


        # if not lists:
        #     return None

        # res = ListNode(0)
        # cur = res

        # while True:
        #     min_node = -1
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue
        #         if min_node == -1 or lists[i].val < lists[min_node].val:
        #             min_node = i
            
        #     if min_node == -1:
        #         break
            
        #     cur.next = lists[min_node]
        #     lists[min_node]  = lists[min_node].next
        #     cur = cur.next

        # return res.next 


