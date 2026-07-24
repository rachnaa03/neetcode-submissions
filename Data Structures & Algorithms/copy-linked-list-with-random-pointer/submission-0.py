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

        old_to_new = {}
        temp = head

        while temp:
            copy = Node(temp.val)
            old_to_new[temp] = copy
            temp = temp.next

        temp = head
        while temp:
            copy = old_to_new[temp]
            
            if temp.next:
                copy.next = old_to_new[temp.next]

            if temp.random:
                copy.random = old_to_new[temp.random]

            temp = temp.next
                
        return old_to_new[head]
            