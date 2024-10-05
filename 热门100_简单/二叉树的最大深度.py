# Definition for a binary tree node.
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
"""


class Solution:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        """DFS 后序遍历 递归"""
        # leftMax = self.maxDepth(root.left)
        # rightMax = self.maxDepth(root.right)
        # return 1 + max(leftMax, rightMax)

        """BFS 层序遍历 队列"""
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res


# test
# 创建测试用例
@pytest.fixture
def solution():
    return Solution()


# 测试空树
def test_empty_tree(solution):
    assert solution.maxDepth(None) == 0


# 测试单个节点
def test_single_node(solution):
    root = TreeNode(1)
    assert solution.maxDepth(root) == 1


# 测试只有左子树的树
def test_left_only_tree(solution):
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert solution.maxDepth(root) == 2


# 测试只有右子树的树
def test_right_only_tree(solution):
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert solution.maxDepth(root) == 2


# 测试平衡二叉树
def test_balanced_tree(solution):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    assert solution.maxDepth(root) == 3


# 测试不平衡二叉树
def test_unbalanced_tree(solution):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right.right = TreeNode(3)
    assert solution.maxDepth(root) == 4
