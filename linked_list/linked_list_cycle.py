# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle in it.

        Args:
            head (Optional[ListNode]): The head of the singly-linked list.

        Returns:
            bool: True if there is a cycle in the linked list, False otherwise.

        Example:
            >>> head_node = ListNode(3)
            >>> head_node.next = ListNode(2)
            >>> head_node.next.next = ListNode(0)
            >>> head_node.next.next.next = ListNode(-4)
            >>> head_node.next.next.next.next = head_node.next
            >>> Solution().hasCycle(head_node)
            True
        """
        if not head:
            return False

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
