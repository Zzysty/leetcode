from typing import List, Optional

import pytest

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        不返回任何内容，而是就地修改 nums。
            1.先将 nums 中的0去掉，并返回去除0后的数组长度
            2.将 nums 剩余部分全部置为0
        """
        # 非0元素个数
        length = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[length] = nums[i]
                length += 1
        # 2.将 nums 剩余部分全部置为0
        for i in range(length, len(nums)):
            nums[i] = 0


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Case 1: 常规用例
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),

        # Case 2: 全是零
        ([0, 0, 0], [0, 0, 0]),

        # Case 3: 没有零
        ([1, 2, 3], [1, 2, 3]),

        # Case 4: 零在开头
        ([0, 0, 1, 2, 3], [1, 2, 3, 0, 0]),

        # Case 5: 零在结尾
        ([1, 2, 3, 0, 0], [1, 2, 3, 0, 0]),

        # Case 6: 零夹在中间
        ([4, 0, 5, 0, 6], [4, 5, 6, 0, 0]),

        # Case 7: 单个元素，非零
        ([5], [5]),

        # Case 8: 单个元素，零
        ([0], [0]),

        # Case 9: 混合正负零
        ([0, -1, 0, 2, -3], [-1, 2, -3, 0, 0]),
    ]
)
def test_move_zeroes(nums, expected):
    solution = Solution()
    solution.moveZeroes(nums)
    assert nums == expected
