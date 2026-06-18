# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = fast = slow = head
        
        count = 0
        if not head:
            return None
        if not head.next:
            return None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if count>=1:
                prev = prev.next
            count += 1
        if prev.next.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        return head
        