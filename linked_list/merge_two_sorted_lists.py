# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted singly-linked lists into one sorted singly-linked list.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted singly-linked list.
            list2 (Optional[ListNode]): The head of the second sorted singly-linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted singly-linked list.

        Example:
            >>> list1 = ListNode(1, ListNode(2, ListNode(4)))
            >>> list2 = ListNode(1, ListNode(3, ListNode(4)))
            >>> Solution().mergeTwoLists(list1, list2)
            ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

        """
        curr_node = pre_head_node = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                curr_node.next, list1 = list1, list1.next
            else:
                curr_node.next, list2 = list2, list2.next
            curr_node = curr_node.next
        curr_node.next = list1 or list2
        return pre_head_node.next
