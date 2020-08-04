# Q.1)https://leetcode.com/problems/middle-of-the-linked-list/

class Node:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    cur = head
    first=True
    while cur != None:
        if first:
            print(cur.val, end='')
            first=False
        else:
            print(', '+str(cur.val), end='')
        cur = cur.next

def addElementToEndOfTheLL(head, x):
    if head is None:
        return Node(x)

    cur = head
    while cur.next != None:
        cur = cur.next
    cur.next = Node(x)
    return head

class Solution:
    def middleNode(self, head):
        if(head == None):
            return head
        prev = curr = head
        while curr != None and curr.next != None:
            prev = prev.next
            curr = curr.next.next
        return prev



if __name__=="__main__":
    lst=input()
    lst=lst.split()
    lNode=None
    print("[",end='')
    for idx in range(0,len(lst)):
        lNode=addElementToEndOfTheLL(lNode, int(lst[idx]))
    sol=Solution()
    val=sol.middleNode(lNode)
    printLinkedList(val)
    print("]")