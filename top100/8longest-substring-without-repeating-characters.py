"""
3. 无重复字符的最长子串
已解答
中等
相关标签
premium lock icon
相关企业
提示
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

面试中遇到过这道题?
1/5
是
否
通过次数
4,091,386/9.7M
通过率
42.2%
相关标签
中级工程师
哈希表
字符串
滑动窗口
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = dict()
        m = 0
        for i, char in enumerate(s):
            if char not in h:
                h[char] = i
                continue
            m = max(m, len(h))
            for key in list(h.keys()):
                if key == char:
                    h.pop(key)
                    h[char] = i
                    break
                h.pop(key)
        m = max(m, len(h))
        return m



if __name__ == "__main__":
    s = "abcabcbb"
    s = 'bbbbb'
    s = 'pwwkew'
    solu = Solution()
    print(solu.lengthOfLongestSubstring(s))
