"""
151. 翻转字符串里的单词
给你一个字符串 s ，逐个翻转字符串中的所有 单词 。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

说明：

输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
翻转后单词间应当仅用一个空格分隔。
翻转后的字符串中不应包含额外的空格。


示例 1：

输入：s = "the sky is blue"
输出："blue is sky the"
示例 2：

输入：s = "  hello world  "
输出："world hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是翻转后的字符不能包括。
示例 3：

输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，将翻转后单词间的空格减少到只含一个。
示例 4：

输入：s = "  Bob    Loves  Alice   "
输出："Alice Loves Bob"
示例 5：

输入：s = "Alice does not even like bob"
输出："bob like even not does Alice"


提示：

1 <= s.length <= 104
s 包含英文大小写字母、数字和空格 ' '
s 中 至少存在一个 单词


进阶：

请尝试使用 O(1) 额外空间复杂度的原地解法。
通过次数156,025提交次数326,468

tag: 双指针 字符串
背诵
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        index = 0
        space_buffer = None
        status = "start"
        while index < len(s):
            ch = s[index]
            if ch.isspace():
                if status == "start":
                    index += 1
                    continue
                if space_buffer is None:
                    space_buffer = ch
            else:
                if status == "start":
                    status = "word"
                if space_buffer is not None:
                    ret.append(space_buffer)
                    space_buffer = None
                ret.append(ch)
            index += 1

        left, right = 0, len(ret) - 1
        self._reverse(ret, left, right)
        for right in range(len(ret)):
            if ret[right].isspace():
                self._reverse(ret, left, right - 1)
                left = right + 1
        self._reverse(ret, left, right)
        return ''.join(ret)

    def _reverse(self, s: list[str], left: int, right: int) -> None:
        while 0 <= left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = "the sky is blue"
    s = "  hello world  "
    x = Solution()
    print(x.reverseWords(s))
