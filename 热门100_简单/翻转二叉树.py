# Definition for a binary tree node.
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root


def tree_to_list(root):
    """Helper function to convert tree to list for easy comparison."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values to match expected format
    while result and result[-1] is None:
        result.pop()
    return result


def build_tree(values):
    """Helper function to build tree from list."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while index < len(values):
        node = queue.pop(0)
        if node:
            if index < len(values) and values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)
            index += 1
    return root


@pytest.mark.parametrize(
    "input_tree, expected_output",
    [
        # Case 1: Full binary tree
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),

        # Case 2: Tree with only one node
        ([1], [1]),

        # Case 3: Empty tree
        ([], []),

        # Case 4: Skewed tree (left-leaning)
        ([1, 2, None, 3], [1, None, 2, None, 3]),

        # Case 5: Skewed tree (right-leaning)
        ([1, None, 2, None, 3], [1, 2, None, 3]),
    ]
)
def test_invert_tree(input_tree, expected_output):
    solution = Solution()
    # Build the input tree from list
    root = build_tree(input_tree)
    # Invert the tree
    inverted_root = solution.invertTree(root)
    # Convert the inverted tree back to list
    result = tree_to_list(inverted_root)
    # Assert the inverted tree matches the expected output
    assert result == expected_output
