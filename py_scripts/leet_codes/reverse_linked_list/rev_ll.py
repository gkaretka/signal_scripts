# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c_node = head.next
        p_node = head
        head.next = None

        while c_node != None:
            n_node = c_node.next
            c_node.next = p_node
            p_node = c_node
            c_node = n_node

        head = p_node

        return head

    def reverseListV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head:
            head.next, rev, head = rev, head, head.next
        return rev

head = ListNode()
c_node = head
for i in range(1, 5):
    nn = ListNode(i)
    c_node.next = nn
    c_node = nn

node = head
while node != None:
    print(node.val)
    node = node.next

a = Solution()

head = a.reverseListV2(head)
node = head
while node != None:
    print(node.val)
    node = node.next
