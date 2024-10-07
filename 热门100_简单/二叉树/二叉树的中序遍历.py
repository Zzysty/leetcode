# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 中序遍历：左-根-右
        """递归"""
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

def test_inorder_traversal():
    # 创建测试用例
    # 二叉树结构如下：
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 创建解决方案实例
    solution = Solution()

    # 执行测试
    result = solution.inorderTraversal(root)
    expected = [4, 2, 5, 1, 3]
    assert result == expected, f"Expected {expected}, but got {result}"

    # 另一个测试用例
    # 二叉树结构如下：
    #     6
    #    / \
    #   7   8
    root2 = TreeNode(6)
    root2.left = TreeNode(7)
    root2.right = TreeNode(8)

    # 执行测试
    result2 = solution.inorderTraversal(root2)
    expected2 = [7, 6, 8]
    assert result2 == expected2, f"Expected {expected2}, but got {result2}"