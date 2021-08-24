"""
718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。



示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。


提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
通过次数77,271提交次数137,020

tag: 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希
"""
from typing import List


class Solution:
    def findLengthFoolish(self, nums1: List[int], nums2: List[int]) -> int:
        sub_list1 = self.get_sub_list(nums1)
        sub_list2 = self.get_sub_list(nums2)
        ret = 0
        for subs1 in sub_list1:
            for subs2 in sub_list2:
                for sub1 in subs1:
                    for sub2 in subs2:
                        if sub1 == sub2 and len(sub1) > ret:
                            ret = len(sub1)
        return ret

    def get_sub_list(self, nums: List[int]):
        if not nums:
            return []
        ret = []
        for num in nums[::-1]:
            if not ret:
                ret.append([[num]])
            else:
                tmp = []
                for sub in ret[-1]:
                    _ = [num]
                    _.extend(sub[:])
                    tmp.append(_)
                tmp.append([num])
                ret.append(tmp)
        return ret

if __name__ == '__main__':
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    s = Solution()
    print(s.findLengthFoolish(nums1,nums2))
