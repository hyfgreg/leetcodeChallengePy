"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]


提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
通过次数377,046提交次数482,232

tag: 数组 回溯
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums[:]]
        ans = []
        for index in range(len(nums)):
            sub_ans = self.permute(nums[:index] + nums[index + 1:])
            for _ans in sub_ans:
                ans.append([nums[index]] + _ans)
        return ans


if __name__ == '__main__':
    nums = [1, 2,3,4]
    s = Solution()
    print(s.permute(nums))
