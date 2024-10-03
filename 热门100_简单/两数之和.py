from typing import List


def twosum(nums: List[int], target: int) -> List[int]:

    """循环遍历"""
    # nums_len = len(nums)
    # for i in range(nums_len):
    #     for j in range(i + 1, nums_len):
    #         if nums[i] + nums[j] == target:
    #             print(f'[{i},{j}]')
    #             return [i, j]

    """哈希表，字典"""
    hashtable = {}
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
twosum(nums, target)
