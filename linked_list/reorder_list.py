# https://leetcode.com/problems/reorder-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders a singly-linked list in-place such that the nodes are rearranged in a specific order.

        The order is: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

        Args:
            head (Optional[ListNode]): The head of the singly-linked list.

        Returns:
            None: This function modifies the list in-place and does not return anything.

        Example:
            >>> head_node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
            >>> Solution().reorderList(head_node)
            >>> # The list is now reordered to 1 → 4 → 2 → 3
        """
        if not head or not head.next:
            return

        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Merge the two halves
        first_half, second_half = head, prev
        while second_half:
            first_half.next, first_half = second_half, first_half.next
            second_half.next, second_half = first_half, second_half.next
