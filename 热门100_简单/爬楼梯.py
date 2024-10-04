"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

思路：拆解为子问题，状态方程同 斐波那契数列
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # 初始化dp数组，长度为n+1，因为我们需要计算dp[n]
        dp = [0] * (n + 1)
        # 基本情况
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# test
def test_climbStairs():
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
