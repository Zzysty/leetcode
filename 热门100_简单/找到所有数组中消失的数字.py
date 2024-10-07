from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)   # [1,n] 范围
        """暴力 循环添加再删除"""
        # a = [] * n
        # for i in range(n):
        #     a.append(i+1)
        # for i in nums:
        #     if i in a:
        #         a.remove(i)
        # return a

        """set"""
        a = set(nums) # 去重
        b = set(range(1,n+1))
        return list(b-a)


s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))