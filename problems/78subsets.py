"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
通过次数297,519提交次数371,592

tag: 位运算 数组 回溯
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(len(nums) - 1, -1, -1):
            tmp = []
            for sub in ret:
                tmp.append([nums[i]] + sub[:])
            tmp.append([nums[i]])
            ret.extend(tmp)
        ret.append([])
        return ret

if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.subsets(nums))
