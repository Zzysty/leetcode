from typing import List, Optional

import pytest

"""
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """快慢指针，相遇则有环"""
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


# 创建测试用例
@pytest.fixture
def solution():
    return Solution()


# 测试有环链表
def test_hasCycle_with_cycle():
    # 构建链表 1 -> 2 -> 3 -> 4 -> 2 (形成环)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 从节点4回到节点2形成环

    solution = Solution()
    assert solution.hasCycle(node1) == True, "应该检测到链表中有环"


# 测试无环链表
def test_hasCycle_without_cycle():
    # 构建链表 1 -> 2 -> 3 -> 4 (无环)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # 链表结束，无环

    solution = Solution()
    assert solution.hasCycle(node1) == False, "应该检测到链表中无环"


# 测试空链表
def test_hasCycle_empty_list():
    solution = Solution()
    assert solution.hasCycle(None) == False, "应该检测到空链表中无环"


# 测试单个节点链表
def test_hasCycle_single_node():
    node = ListNode(1)
    solution = Solution()
    assert solution.hasCycle(node) == False, "应该检测到单个节点的链表中无环"
