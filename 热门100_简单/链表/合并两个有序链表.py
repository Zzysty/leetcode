from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy

        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next

        p.next = p1 or p2  # 剩余元素，谁不为空就接谁

        return dummy.next



def test_mergeTwoLists():
    # 创建链表1: 1 -> 2 -> 4
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    # 创建链表2: 1 -> 3 -> 4
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    sol = Solution()
    merged_list = sol.mergeTwoLists(l1, l2)

    # 验证合并后的链表是否正确
    expected_values = [1, 1, 2, 3, 4, 4]
    actual_values = []
    while merged_list is not None:
        actual_values.append(merged_list.val)
        merged_list = merged_list.next

    assert actual_values == expected_values, f"Expected {expected_values}, but got {actual_values}"
