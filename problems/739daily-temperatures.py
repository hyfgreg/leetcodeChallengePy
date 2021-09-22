"""
739. 每日温度
请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。

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
通过次数207,342提交次数305,345

tag: 栈 数组 单调栈
背诵 牛逼，我自己做出来的！
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        ret = [0 for _ in range(length)]
        for index, t in enumerate(temperatures[::-1]):
            index = length - index - 1
            while stack and stack[-1][1] <= t:
                stack.pop()
            tmp = 0 if not stack else stack[-1][0] - index
            stack.append((index, t))
            # print(f"{tmp}, {index}, {t}, {stack[:-1]}, {stack}")
            ret[index] = tmp
        return ret


if __name__ == '__main__':
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(temperatures))
    temperatures = [30,40,50,60]
    print(s.dailyTemperatures(temperatures))
