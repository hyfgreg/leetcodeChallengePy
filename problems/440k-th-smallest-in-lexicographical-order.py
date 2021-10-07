"""
440. 字典序的第K小数字
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
通过次数16,505提交次数43,412

tag: 字典树
第一次见
背诵
"""
from typing import List


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_count(prefix, n):
            next_prefix = prefix + 1
            count = 0
            while prefix <= n:
                count += min(n + 1, next_prefix) - prefix
                prefix *= 10
                next_prefix *= 10
            return count

        p = 1
        prefix = 1
        while p < k:
            count = get_count(prefix, n)
            # print(f"p {p}, prefix {prefix}, n {n}, count {count}")
            if p + count > k:
                prefix *= 10
                p += 1
            else:
                prefix += 1
                p += count
        return prefix


if __name__ == '__main__':
    n = 12
    s = Solution()
    print(s.findKthNumber(20, 4))
