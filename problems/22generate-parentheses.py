"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

有效括号组合需满足：左括号必须以正确的顺序闭合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

n = 2
输出：["(())","()()"]

输入：n = 1
输出：["()"]


提示：

1 <= n <= 8
通过次数334,018提交次数432,405

tag: 字符串 动态规划 回溯

背诵
"""
from typing import List


class Solution:
    ret = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.parent('', n, n)
        return self.ret

    def parent(self, ans: str, left: int, right: int):
        if left == right == 0:
            self.ret.append(ans)
            return
        if left != 0 and right == 0:
            return
        if left == right:
            return self.parent(ans + '(', left - 1, right)
        if left == 0:
            return self.parent(ans + ')', left, right - 1)
        self.parent(ans + '(', left - 1, right)
        self.parent(ans + ')', left, right - 1)


if __name__ == '__main__':
    s = Solution()
    n = 1
    print(s.generateParenthesis(1))
