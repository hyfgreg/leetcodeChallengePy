"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。



示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
通过次数214,931提交次数337,166

tag: 数组 回溯
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        ret = []
        head = set() # todo 用这个东西来去重！
        for i in range(len(nums)):
            if nums[i] in head:
                continue
            tmp = [nums[i]]
            head.add(nums[i])
            sub_rets = self.permuteUnique(nums[:i] + nums[i + 1:])
            for sub in sub_rets:
                ret.append(tmp + sub)
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.permuteUnique(nums))
