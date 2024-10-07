# Definition for a binary tree node.
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
检查二叉树是否轴对称

特例处理： 若根节点 root 为空，则直接返回 true 。
返回值： 即 recur(root.left, root.right) ;
函数 recur(L, R) ：

终止条件：
当 L 和 R 同时越过叶节点： 此树从顶至底的节点都对称，因此返回 true 。
当 L 或 R 中只有一个越过叶节点： 此树不对称，因此返回 false 。
当节点 L 值 /节点 R 值： 此树不对称，因此返回 false 。
递推工作：
判断两节点 L.left 和 R.right 是否对称，即 recur(L.left, R.right) 。
判断两节点 L.right 和 R.left 是否对称，即 recur(L.right, R.left) 。
返回值： 两对节点都对称时，才是对称树，因此用与逻辑符 && 连接。
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(L, R):
            # 左右子树为空
            if not L and not R:
                return True
            # 左右子树深度不一致或者值不相同
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)    # 递归

        return not root or recur(root.left, root.right)


# test
# 创建测试用例
@pytest.fixture
def solution():
    return Solution()

# 测试空树
def test_empty_tree(solution):
    assert solution.isSymmetric(None) == True

# 测试单个节点
def test_single_node(solution):
    root = TreeNode(1)
    assert solution.isSymmetric(root) == True

# 测试对称树
def test_symmetric_tree(solution):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    assert solution.isSymmetric(root) == True

# 测试不对称树
def test_asymmetric_tree(solution):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    assert solution.isSymmetric(root) == False