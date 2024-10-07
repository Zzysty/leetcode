from typing import List, Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA


# 创建测试用例
@pytest.fixture
def solution():
    return Solution()


# 测试有交点的链表
def test_getIntersectionNode_with_intersection(solution):
    # 构建链表 A: 1 -> 2 -> 3 -> 4 -> 5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # 构建链表 B: 6 -> 7 -> 8 -> 9 -> 3 (与链表 A 交于节点 3)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node3

    assert solution.getIntersectionNode(node1, node6) == node3, "应该检测到交点为节点 3"


# 测试无交点的链表
def test_getIntersectionNode_without_intersection(solution):
    # 构建链表 A: 1 -> 2 -> 3 -> 4 -> 5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # 构建链表 B: 6 -> 7 -> 8 -> 9
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node6.next = node7
    node7.next = node8
    node8.next = node9

    assert solution.getIntersectionNode(node1, node6) is None, "应该检测到链表中无交点"


# 测试空链表
def test_getIntersectionNode_empty_lists(solution):
    assert solution.getIntersectionNode(None, None) is None, "应该检测到空链表中无交点"


# 测试单个节点链表
def test_getIntersectionNode_single_nodes(solution):
    nodeA = ListNode(1)
    nodeB = ListNode(2)

    assert solution.getIntersectionNode(nodeA, nodeB) is None, "应该检测到单个节点的链表中无交点"
