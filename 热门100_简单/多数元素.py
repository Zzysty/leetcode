from typing import List

import pytest

"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """异或"""
        # x = 0
        # for num in nums:  # 1. 遍历 nums 执行异或运算
        #     x ^= num
        # return x  # 2. 返回出现一次的数字 x

        """暴力法"""
        count_dict = {}
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        max_value = max(count_dict, key=lambda k: count_dict[k])
        return max_value


# 创建测试用例
@pytest.fixture
def solution():
    return Solution()


def test_majorityElement(solution):
    nums = [3, 2, 3]
    assert solution.majorityElement(nums) == 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    assert solution.majorityElement(nums) == 2
