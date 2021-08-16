"""
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。



注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。


提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成


进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

tag: 哈希 字符串 滑动窗
背诵
todo: 可以外层for来实现right移动，内层for实现left移动
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        current = {}
        valid = 0
        for i in t:
            if i in target:
                target[i] += 1
            else:
                current[i] = 0
                target[i] = 1
                valid += 1

        print(f"target {target} current {current}")

        def is_covered():
            nonlocal target, current
            for ch in target:
                if current[ch] < target[ch]:
                    return False
            return True

        left, right = 0, 0
        ans = ""
        tmp = ""
        v = 0
        while left < len(s) and right < len(s):
            # 1. 滑动right，直到覆盖
            print(f"left {left},right {right}")
            print("move right")
            while right < len(s):
                if s[right] in current:
                    current[s[right]] += 1
                    if current[s[right]] == target[s[right]]:
                        v += 1
                    if v == valid:
                        tmp = s[left:right + 1]
                        break
                right += 1
            print(f"move right over, left {left} right {right} ans {ans}")
            print("move left")
            # return
            # 2. 滑动left， 直到不覆盖
            while left <= right:
                if s[left] in current:
                    if current[s[left]] == target[s[left]]:
                        v -= 1
                    current[s[left]] -= 1
                left += 1
                if v < valid:
                    break
                if tmp:
                    tmp = s[left:right + 1]
            print("tmp", tmp)
            if tmp:
                if not ans:
                    ans = tmp
                elif len(tmp) < len(ans):
                    ans = tmp
            tmp = ""
            print("move left over, ans", ans)
            right += 1
        return ans


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "a"
    # t = "aa"
    # s = "ab"
    # t = "a"
    # s = "aa"
    # t = "aa"
    s = "bdab"
    t = "ab"
    # s = "acbbaca"
    # t = "aba"
    ss = Solution()
    print(ss.minWindow(s, t))
