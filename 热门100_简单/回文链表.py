from typing import List, Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 将链表节点的值存储到列表中
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next

        # 判断列表是否是回文
        return vals == vals[::-1]


def build_linked_list(values):
    """Helper function to build linked list from list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


import pytest


@pytest.mark.parametrize(
    "values, expected",
    [
        # 单节点链表
        ([1], True),

        # 双节点链表，回文
        ([1, 1], True),

        # 双节点链表，不是回文
        ([1, 2], False),

        # 奇数个节点，回文
        ([1, 2, 1], True),

        # 奇数个节点，不是回文
        ([1, 2, 3], False),

        # 偶数个节点，回文
        ([1, 2, 2, 1], True),

        # 偶数个节点，不是回文
        ([1, 2, 3, 4], False),

        # 空链表，视为回文
        ([], True),

        # 长链表，回文
        ([1, 2, 3, 4, 3, 2, 1], True),

        # 长链表，不是回文
        ([1, 2, 3, 4, 5, 2, 1], False),
    ]
)
def test_is_palindrome(values, expected):
    solution = Solution()
    head = build_linked_list(values)
    assert solution.isPalindrome(head) == expected
