"""
93. 复原 IP 地址
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。



示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


提示：

0 <= s.length <= 3000
s 仅由数字组成

tag: 字符串 回溯
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restore(s, 4)

    def restore(self, s: str, count: int) -> List[str]:
        if len(s) < count:
            return []
        if count < 1:
            return []
        if count == 1:
            if len(s) > 3:
                return []
            if s[0] == '0' and len(s) > 1:
                return []
            if int(s) > 255:
                return []
            return [s]
        ret = []
        tmp = []
        if s[0] == '0':
            tmp.append([s[0], s[1:]])
        else:
            tmp.append([s[:1], s[1:]])
            tmp.append([s[:2], s[2:]])
            if int(s[:3]) <= 255:
                tmp.append([s[:3], s[3:]])
        for head, tail in tmp:
            tail_ret_list = self.restore(tail, count - 1)
            if tail_ret_list:
                for tail_ret in tail_ret_list:
                    ret.append('.'.join([head, tail_ret]))
        return ret


if __name__ == '__main__':
    solution = Solution()
    s = "25525511135"
    print(solution.restoreIpAddresses(s))
    s = "0000"
    print(solution.restoreIpAddresses(s))
    s = "010010"
    print(solution.restoreIpAddresses(s))
    s = "101023"
    print(solution.restoreIpAddresses(s))
