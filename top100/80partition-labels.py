"""763. 划分字母区间
中等
相关标签
premium lock icon
相关企业
提示
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

返回一个表示每个字符串片段的长度的列表。



示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
示例 2：

输入：s = "eccbbbbdec"
输出：[10]


提示：

1 <= s.length <= 500
s 仅由小写英文字母组成

面试中遇到过这道题?
1/5
是
否
通过次数
491,613/622.5K
通过率
79.0%
相关标签
贪心
哈希表
双指针
字符串
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        i = 0
        first_alpha = dict()
        last_alpha = dict()
        ret = []
        for i in range(n):
            # 新字母
            if s[i] not in first_alpha:
                first_alpha[s[i]] = i
            last_alpha[s[i]] = i
        span = None
        for start, end in zip(first_alpha.values(), last_alpha.values()):
            if not span:
                span = [start, end]
            elif span[0] < end < span[-1]:
                continue
            elif span[0] < start < span[-1] < end:
                span[1] = end
            else:
                ret.append(span[1] - span[0] + 1)
                span = [start, end]
        if span:
            ret.append(span[1] - span[0] + 1)
        return ret

    def partitionLabelsLeetcode(self, s: str) -> List[int]:
        n = len(s)
        last_alpha = dict()
        ret = []
        for i in range(n):
            # 新字母
            last_alpha[s[i]] = i
        start = 0
        end = 0
        for i in range(n):
            end = max(
                end, last_alpha[s[i]]
            )  # 这里和我自己的span其实是一个意思，end要么我自己，要么是之后还有其他出现在之前的字母
            # 如果当前span最大位置就是我自己，说明这个span的边界就是我自己
            if end == i:
                ret.append(end - start + 1)
                start = end + 1
        return ret


if __name__ == "__main__":
    solu = Solution()
    s = "ababcbacadefegdehijhklij"
    s = "eccbbbbdec"
    print(s)
    print(solu.partitionLabelsLeetcode(s))
