from typing import Optional

import pytest

"""
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 当前节点的直径等于左右子树深度之和
        max_diameter = 0
        def dfs(root):
            nonlocal max_diameter
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            max_diameter = max(max_diameter, left + right)
            return max(left, right) + 1
        dfs(root)
        return max_diameter


@pytest.fixture
def example_trees():
    # 构建示例树1
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # 最大直径为 3（路径是 4 -> 2 -> 1 -> 3 或 5 -> 2 -> 1 -> 3）
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    # 构建示例树2
    #     1
    #    /
    #   2
    #  /
    # 3
    # 最大直径为 2（路径是 3 -> 2 -> 1）
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)

    # 构建示例树3（单节点）
    #     1
    # 最大直径为 0
    root3 = TreeNode(1)

    # 构建空树
    root4 = None

    return [
        (root1, 3),  # (树, 期望的直径)
        (root2, 2),
        (root3, 0),
        (root4, 0),
    ]

def test_diameter_of_binary_tree(example_trees):
    for tree, expected_diameter in example_trees:
        assert Solution().diameterOfBinaryTree(tree) == expected_diameter
