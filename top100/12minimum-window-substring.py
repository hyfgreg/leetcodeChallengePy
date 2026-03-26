"""76. 最小覆盖子串
困难
相关标签
premium lock icon
相关企业
提示
给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。

测试用例保证答案唯一。



示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。


提示：

m == s.length
n == t.length
1 <= m, n <= 105
s 和 t 由英文字母组成


进阶：你能设计一个在 O(m + n) 时间内解决此问题的算法吗？

面试中遇到过这道题?
1/5
是
否
通过次数
1,035,303/2.1M
通过率
49.1%
相关标签
哈希表
字符串
滑动窗口
"""

"""
双指针，滑动窗！！！没有那么难的！！！
一个有趣的哈希方法
一个dict+一个整数，target和need，与windows和have对比，来判断是否包含子串
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not s:
            return ""
        target = dict()
        for c in t:
            target[c] = target.get(c, 0) + 1

        window = dict()
        need = len(target)
        left = 0
        right = 0
        have = 0

        min_start = 0
        min_len = float("inf")
        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in target and target[c] == window[c]:
                have += 1
            while have == need:
                # 更新最小索引和长度
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                c = s[left]
                window[c] -= 1
                if c in target and window[c] < target[c]:
                    have -= 1
                left += 1
            right += 1
        return s[min_start : min_start + min_len] if min_len != float("inf") else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    res = "BANC"
    # s = "a"
    # t = "aa"
    # s = "bdab"
    # t = "ab"
    # s = "aaflslflsldkalskaaa"
    # t = "aaa"
    # s = "abcabdebac"
    # t = "cda"
    solu = Solution()
    print(solu.minWindow(s, t))
