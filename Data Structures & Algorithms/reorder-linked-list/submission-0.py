# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return

        # 1. Find the middle and split into 2 halves
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        # 2. Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Merge the two halves
        p1 = head
        p2 = prev     
        
        while p1 and p2:
            firstNext = p1.next
            secondNext = p2.next
            p1.next = p2
            p2.next = firstNext

            p1 = firstNext
            p2 = secondNext


