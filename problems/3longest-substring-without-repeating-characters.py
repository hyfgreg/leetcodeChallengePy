"""
tag: 哈希表 双指针 字符串 滑动窗

给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。


示例1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0


提示：

0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        length = len(s)
        max_len = 0
        window = {}
        while right < length:
            c = s[right]
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
            right += 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            max_len = max(max_len, right - left)
        return max_len


if __name__ == '__main__':
    a = ['abcabcbb', 'bbbbb', 'pwwkew', '']
    test = Solution()
    for s in a:
        print(s, test.lengthOfLongestSubstring(s))
