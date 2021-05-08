"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

EXAMPLE

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        newList = ListNode(0)
        cur = newList
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            cur.next = l1 or l2  # add non-empty list
        return newList.next