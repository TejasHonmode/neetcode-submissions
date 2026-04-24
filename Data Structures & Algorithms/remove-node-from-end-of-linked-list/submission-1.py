# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        N = 0
        while curr:
            curr = curr.next
            N+=1
        
        removeIndex = N - n
        if removeIndex == 0:
            return head.next
        
        curr = head
        while removeIndex > 1:
            removeIndex -=1
            curr = curr.next
        curr.next = curr.next.next

        return head