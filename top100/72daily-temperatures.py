"""739. 每日温度
中等
相关标签
premium lock icon
相关企业
提示
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。



示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]


提示：

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

面试中遇到过这道题?
1/5
是
否
通过次数
960,857/1.4M
通过率
69.7%
相关标签
栈
数组
单调栈
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack or t < stack[-1][1]:
                stack.append((i, t))
                continue
            while stack and t > stack[-1][1]:
                j, _ = stack.pop()
                ret[j] = i - j
            stack.append((i, t))
        return ret


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solu = Solution()
    print(solu.dailyTemperatures(temperatures))
