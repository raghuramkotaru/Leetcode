# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = slow = head
        prev = None
        
        
        if not head:
            return None
        if not head.next:
            return None
        while fast and fast.next:
            prev= slow
            fast = fast.next.next
            slow = slow.next
            
            
        if prev.next.next:
            prev.next = slow.next
        else:
            prev.next = None
        return head
        