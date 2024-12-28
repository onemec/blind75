# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of a singly-linked list and returns the head of the modified list.

        Args:
            head (Optional[ListNode]): The head of the singly-linked list.
            n (int): The position of the node to remove from the end of the list.

        Returns:
            Optional[ListNode]: The head of the modified singly-linked list.

        Example:
            >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            >>> Solution().removeNthFromEnd(head, 2)
            ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        """
        dummy_head = ListNode(0, head)
        slow_pointer, fast_pointer = dummy_head, head
        for _ in range(n):
            fast_pointer = fast_pointer.next
        while fast_pointer:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        slow_pointer.next = slow_pointer.next.next
        return dummy_head.next
