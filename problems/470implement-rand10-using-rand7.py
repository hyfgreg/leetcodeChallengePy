"""
470. 用 Rand7() 实现 Rand10()
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。



示例 1:

输入: 1
输出: [7]
示例 2:

输入: 2
输出: [8,4]
示例 3:

输入: 3
输出: [8,1,10]


提示:

rand7 已定义。
传入参数: n 表示 rand10 的调用次数。


进阶:

rand7()调用次数的 期望值 是多少 ?
你能否尽量少调用 rand7() ?
通过次数31,097提交次数56,116

tag: 数学 拒绝采样 概率与统计 随机化
背诵？
用rand10 求 rand7
算法:
while True:
    num = rand10()
    if num <= 7:
        return num
数学证明:
以1为例，求1在以上算法中的概率
P(1) = 1/10 + (3/10) * (1/10) + (3/10)*(3/10)*(1/10) + ... + (3/10)^n*(1/10)
     = 1/10 * (1 + 3/10 + (3/10)^2 + ... + (3/10)^n) # 等比数列求和
     = 1/10 * (1 + (3/10)*(1-(3/10)^n)/(1-3/10))
     = 1/10 * (1+(3/10)/(7/10)) # n趋近于无穷时
     = 1/7
这里注意，第n(n>1)次随机到1的概率，不能是(9/10)^n-1 * (1/10)，因为9/10包含了随机到2-7的概率，这个是不对的

第二个关键点:
rand_mn -> rand_n
mn % n + 1即可

例如
rand_40 -> rand_10
rand_40 % 10 + 1
"""

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random


def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1
            num = (num - 40 - 1) * 7 + rand7()
            if num <= 60:
                return num % 10 + 1
            num = (num - 60 - 1) * 7 + rand7()
            if num <= 20:
                return num % 10 + 1
