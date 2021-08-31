"""
165. 比较版本号
给你两个版本号 version1 和 version2 ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。

返回规则如下：

如果 version1 > version2 返回 1，
如果 version1 < version2 返回 -1，
除此之外返回 0。


示例 1：

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"
示例 2：

输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有指定下标为 2 的修订号，即视为 "0"
示例 3：

输入：version1 = "0.1", version2 = "1.1"
输出：-1
解释：version1 中下标为 0 的修订号是 "0"，version2 中下标为 0 的修订号是 "1" 。0 < 1，所以 version1 < version2
示例 4：

输入：version1 = "1.0.1", version2 = "1"
输出：1
示例 5：

输入：version1 = "7.5.2.4", version2 = "7.5.3"
输出：-1


提示：

1 <= version1.length, version2.length <= 500
version1 和 version2 仅包含数字和 '.'
version1 和 version2 都是 有效版本号
version1 和 version2 的所有修订号都可以存储在 32 位整数 中
通过次数53,245提交次数109,454

tag: 双指针 字符串

"""
from itertools import zip_longest
from typing import List


class Solution:
    # todo 可以两个str一起解析，某个str解析完毕之后，如果另一个没解析完就全用'0'
    # todo 比较python的方法就是每次解析完毕后yield一个结果，然后外面的for直接用结果判断
    # TODO 或者可以写一个生成器解析一个str，然后zip_longest两个生成器
    def compareVersion(self, version1: str, version2: str) -> int:
        version_list1 = self.split(version1)
        version_list2 = self.split(version2)
        for sub1, sub2 in zip_longest(version_list1, version_list2):
            if not sub1:
                sub1 = '0'
            if not sub2:
                sub2 = '0'
            sub_compare = self.compare(sub1, sub2)
            if sub_compare != 0:
                return sub_compare
        return 0

    def split(self, version: str) -> List[str]:
        ret = []
        left, right = 0, 0
        length = len(version)
        while right < length:
            if version[right] == '.':
                if left == right:
                    # 说明修订号是0
                    ret.append('0')
                else:
                    ret.append(version[left:right])
                right += 1
                left = right
                continue
            if version[right] == '0' and left == right:
                right += 1
                left = right
                continue
            right += 1
        if left == right:
            ret.append('0')
        else:
            ret.append(version[left:right])
        return ret

    def compare(self, num1: str, num2: str) -> int:
        if len(num1) < len(num2):
            return -1
        if len(num1) > len(num2):
            return 1
        n = len(num1)
        for i in range(n):
            if num1[i] == num2[i]:
                continue
            return -1 if num1[i] < num2[i] else 1
        return 0


if __name__ == '__main__':
    version1 = "1.01"
    version2 = "1.001"
    s = Solution()
    print(s.compareVersion(version1, version2))
