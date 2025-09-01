# https://leetcode.com/problems/reorder-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next_val = next_val


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
        if not head or not head.next_val:
            return

        # Find the middle of the list
        slow, fast = head, head.next_val
        while fast and fast.next_val:
            slow = slow.next_val
            fast = fast.next_val.next_val

        # Reverse the second half of the list
        prev, curr = None, slow.next_val
        slow.next_val = None
        while curr:
            curr.next_val, prev, curr = prev, curr, curr.next_val

        # Merge the two halves
        first_half, second_half = head, prev
        while second_half:
            first_half.next_val, first_half = second_half, first_half.next_val
            second_half.next_val, second_half = first_half, second_half.next_val
