"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
通过次数607,275提交次数1,489,570

tag: 字符串
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = []
        for ch_list in zip(*strs):
            ch_set = set(ch_list)
            if len(ch_set) == 1:
                ret.append(ch_set.pop())
            else:
                break
        return ''.join(ret)

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ''

        def common(str1, str2):
            length = min(str1, str2)
            for i in range(length):
                if str1[i] != str2[i]:
                    return str1[:i]
            return str1[:length]

        prefix = strs[0]
        for str in strs[1:]:
            prefix = common(prefix, str)
            if not prefix:
                return prefix
        return prefix

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        if not strs:
            return ''
        length = len(strs[0])
        for i in range(length):
            ch = strs[0][i]
            for str in strs[1:]:
                if i == len(str) or ch != str[i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
