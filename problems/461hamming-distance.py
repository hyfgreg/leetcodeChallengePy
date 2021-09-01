"""
461. 汉明距离
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。



示例 1：

输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
示例 2：

输入：x = 3, y = 1
输出：1


提示：

0 <= x, y <= 231 - 1
通过次数164,634提交次数202,800

tag: 位运算

背诵 统计1的个数，可以用>>1，右移的方式，统计最右边的1，直到整个数字变成0，也可以用如下的算法(Brian Kernighan)，每次干掉最右边的1，直到整个数字变成0
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return self.count_one(x^y)

    def count_one(self, s:int):
        ret = 0
        while s:
            s &= (s - 1)
            ret += 1
        return ret
