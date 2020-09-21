#Q.1)https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mapping =dict()
        cur=head
        clonedLLhead=None
        prev=None
        while cur != None:
            x=Node(cur.val)
            mapping[cur]=x
            if clonedLLhead is None:
                clonedLLhead=x
                prev=clonedLLhead
                
            else:
                prev.next=x
                prev=prev.next
            cur = cur.next
            
        cur = head
        while cur != None:
            y = mapping[cur]
            if cur.random is not None:
                z=mapping[cur.random]
                y.random = z
                
            cur = cur.next