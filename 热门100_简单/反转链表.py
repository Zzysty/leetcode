from typing import List, Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            # tmp保存下一个节点
            tmp = cur.next
            # 当前节点指向前一个节点
            cur.next = pre
            # pre和cur都向前移动
            pre = cur
            cur = tmp
        return pre


# 创建测试用例
@pytest.fixture
def solution():
    return Solution()


# 测试空链表
def test_reverseList_empty_list(solution):
    assert solution.reverseList(None) is None, "应该返回空链表"


# 测试单个节点链表
def test_reverseList_single_node(solution):
    node = ListNode(1)
    reversed_head = solution.reverseList(node)
    assert reversed_head.val == 1, "单个节点链表反转后应该是它本身"
    assert reversed_head.next is None, "单个节点链表反转后应该是它本身"


# 测试普通链表
def test_reverseList_normal_list(solution):
    # 构建链表 1 -> 2 -> 3 -> 4 -> 5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    reversed_head = solution.reverseList(node1)

    # 检查反转后的链表
    assert reversed_head.val == 5, "反转后的头结点应该是 5"
    assert reversed_head.next.val == 4, "反转后的第二个节点应该是 4"
    assert reversed_head.next.next.val == 3, "反转后的第三个节点应该是 3"
    assert reversed_head.next.next.next.val == 2, "反转后的第四个节点应该是 2"
    assert reversed_head.next.next.next.next.val == 1, "反转后的第五个节点应该是 1"
    assert reversed_head.next.next.next.next.next is None, "反转后的链表最后一个节点的 next 应该是 None"
