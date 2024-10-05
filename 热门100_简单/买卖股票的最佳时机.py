from typing import List

import pytest

"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """暴力循环"""
        res = 0
        length = len(prices)
        for i in range(length):
            for j in range(i + 1, length):
                res = max(res, prices[j] - prices[i])
        return res

        """贪心 维护两个最值"""
        # cost, profit = float('+inf'), 0
        # for price in prices:
        #     cost = min(cost, price)
        #     profit = max(profit, price - cost)
        # return profit

# 创建测试用例
@pytest.fixture
def solution():
    return Solution()

def test_maxProfit(solution):
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5

    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0

    prices = [1, 2, 3, 4, 5]
    assert solution.maxProfit(prices) == 4

    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    assert solution.maxProfit(prices) == 4

    prices = [1]
    assert solution.maxProfit(prices) == 0

    prices = [1, 2]
    assert solution.maxProfit(prices) == 1
