import pytest

"""
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 1.转成二进制
        # 2.循环比较并统计不同的个数
        # x_bin = bin(x)[2:]  # bin() 转为二进制并去掉前缀0b 0b1 -> '1'
        # y_bin = bin(y)[2:]  # 0b100 -> '100'
        # x_len = len(x_bin)
        # y_len = len(y_bin)
        # diff = abs(x_len - y_len)   # 位数差值
        # if x_len > y_len:
        #     y_bin = '0' * diff + y_bin
        # else:
        #     x_bin = '0' * diff + x_bin
        #
        # dist = 0
        # for i in range(len(x_bin)):
        #     if x_bin[i] != y_bin[i]:
        #         dist += 1
        # return dist

        """异或"""
        return bin(x ^ y).count('1')

# 测试用例
@pytest.mark.parametrize("x, y, expected", [
    (1, 4, 2),
    (3, 1, 1),
    (0, 0, 0),
    (1, 1, 0),
    (2, 3, 1),
])

def test_hammingDistance(x, y, expected):
    s = Solution()
    result = s.hammingDistance(x, y)
    assert result == expected, f"Expected {expected}, but got {result}"
