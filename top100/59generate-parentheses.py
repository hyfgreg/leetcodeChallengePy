"""22. 括号生成
中等
相关标签
premium lock icon
相关企业
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]


提示：

1 <= n <= 8

面试中遇到过这道题?
1/5
是
否
通过次数
1,250,234/1.6M
通过率
79.1%
相关标签
字符串
动态规划
回溯
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        tmp = []

        def dfs(left, right):
            nonlocal ret, tmp, n
            if left == n and right == n:
                ret.append("".join(tmp))
                return
            if left < n:
                tmp.append("(")
                dfs(left + 1, right)
                tmp.pop()
            if right < left:
                tmp.append(")")
                dfs(left, right + 1)
                tmp.pop()

        dfs(0, 0)
        return ret


if __name__ == "__main__":
    solu = Solution()
    print(solu.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
