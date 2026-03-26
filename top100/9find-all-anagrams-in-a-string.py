"""
438. 找到字符串中所有字母异位词
已解答
中等
相关标签
premium lock icon
相关企业
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。



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

面试中遇到过这道题?
1/5
是
否
通过次数
985,518/1.8M
通过率
54.6%
相关标签
哈希表
字符串
滑动窗口
"""

from typing import List

"""
有意思的解法，维护一个count，和一个differ，判断子串和p的差值是否为0
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        st = ord("a")
        ans = [0] * 26
        for i in p:
            ans[ord(i) - st] += 1
        curr = [0] * 26
        for i in range(len(p) - 1):
            curr[ord(s[i]) - st] += 1
        ret = []
        for i in range(len(p) - 1, len(s)):
            curr[ord(s[i]) - st] += 1
            if curr == ans:
                ret.append(i - len(p) + 1)
            curr[ord(s[i - len(p) + 1]) - st] -= 1
        return ret

    def findAnagramsDiffer(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ret = []
        count = [0] * 26  # 题目里说了，只有小写字母
        for i in range(len(p)):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1
        differ = [i != 0 for i in count].count(True)
        if differ == 0:
            ret.append(0)
        #print(s, p, differ, count, ret)
        for i in range(len(s) - len(p)):
            if count[ord(s[i]) - 97] == 1:
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:
                differ += 1
            count[ord(s[i]) - 97] -= 1
            #print(i, count)

            if count[ord(s[i + len(p)]) - 97] == -1:
                differ -= 1
            elif count[ord(s[i + len(p)]) - 97] == 0:
                differ += 1
            count[ord(s[i + len(p)]) - 97] += 1
            if differ == 0:
                ret.append(i + 1)
        return ret


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    s = "abab"
    p = "ab"
    #s = "bbbb"
    #p = "b"
    #s = "baa"
    #p = "aa"
    s = "aaaa"
    p = "aaaa"
    solu = Solution()
    print(solu.findAnagramsDiffer(s, p))
