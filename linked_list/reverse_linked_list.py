# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly-linked list.

        Args:
            head (Optional[ListNode]): The head of the singly-linked list.

        Returns:
            Optional[ListNode]: The new head of the reversed singly-linked list.

        Example:
            >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            >>> Solution().reverseList(head)
            ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        """
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev
