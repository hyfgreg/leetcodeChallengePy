"""
0-12共13个数构成一个环，从0出发，每次走1步，走n步回到0共有多少种走法（2020.09 字节跳动-广告-后端）[1]
0-8组成一个圆环，从0出发，每次可以逆时针和顺时针走，走n步能回到0有多少种情况（2020.09 字节跳动-people-后端）[2]
0~9的环，从0出发，N步后能否走回0。（2020.07 字节跳动-电商-后端）[3]
圆环回原点问题 (2020.08 字节跳动-飞书-后端)[4]
圆环上有10个点，编号为0~9。从0点出发，每次可以逆时针和顺时针走一步，问走n步回到0点共有多少种走法。

输入: 2
输出: 2
解释：有2种方案。分别是0->1->0和0->9->0

tag: 动态规划
背诵 和70题爬楼梯有一点像
"""


class Solution:
    def backToOrigin(self, n):
        """
        dp[走了i步][到第j个点]
        :param n:
        :return:
        """
        length = 10
        dp = [[0 for _ in range(length)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(length):
                dp[i][j] = dp[i - 1][(j + 1) % length] + dp[i - 1][(j + length - 1) % length]
        print(dp)
        return dp[n][0]

if __name__ == '__main__':
    s = Solution()
    print(s.backToOrigin(4))
