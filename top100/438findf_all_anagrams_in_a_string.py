"""
438. 找到字符串中所有字母异位词
中等
相关标签
相关企业
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。



示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        target = dict()
        for i in p:
            if i in target:
                target[i] += 1
            else:
                target[i] = 1
        cur = dict()
        ret = []
        left = 0
        # print("target", target)
        for i in range(len(s)):
            # print("1,", i, s[i], cur, left)
            if s[i] not in target:
                left = i + 1
                cur = dict()
                continue
            if s[i] in cur:
                cur[s[i]] += 1
            else:
                cur[s[i]] = 1
            while cur[s[i]] > target[s[i]]:
                cur[s[left]] -= 1
                left += 1
            # print("2,", i, s[i], cur, left)
            if cur == target:
                ret.append(left)
                cur[s[left]] -= 1
                left += 1
            # print("3,", i, s[i], cur, left, ret)
            # print("=====" * 10)

        return ret


if __name__ == '__main__':
    sl = Solution()
    s = "cbaebabacd"
    p = "abc"
    # s = "abab"
    # p = "ab"
    print(sl.findAnagrams(s, p))
