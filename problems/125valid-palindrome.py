"""
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。



示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: "race a car"
输出: false
解释："raceacar" 不是回文串


提示：

1 <= s.length <= 2 * 105
字符串 s 由 ASCII 字符组成
通过次数276,598提交次数584,344

tag: 双指针 字符串
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            if left >= right:
                return True
            a = s[left].lower()
            while right >= 0 and not s[right].isalnum():
                right -= 1
            if left >= right:
                return True
            b = s[right].lower()
            if a != b:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    so = Solution()
    print(so.isPalindrome(s))
    s = "race a car"
    print(so.isPalindrome(s))
