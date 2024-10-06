from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res


import pytest


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, [0]),  # 0的二进制是"0"
        (1, [0, 1]),  # 1的二进制是"1"
        (2, [0, 1, 1]),  # 2的二进制是"10"
        (3, [0, 1, 1, 2]),  # 3的二进制是"11"
        (4, [0, 1, 1, 2, 1]),  # 4的二进制是"100"
        (5, [0, 1, 1, 2, 1, 2]),  # 5的二进制是"101"
        (6, [0, 1, 1, 2, 1, 2, 2]),  # 6的二进制是"110"
        (7, [0, 1, 1, 2, 1, 2, 2, 3]),  # 7的二进制是"111"
        (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2])  # 测试较大的数字
    ]
)
def test_count_bits(n, expected):
    solution = Solution()
    assert solution.countBits(n) == expected
