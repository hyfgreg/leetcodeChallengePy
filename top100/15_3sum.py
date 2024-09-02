"""
15. 三数之和
中等
相关标签
相关企业
提示
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。





示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。


提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 这里不返回索引，所以顺序无所谓，同时有要求不重复，排序后才能快速去重
        count = len(nums)
        nums.sort()
        print("nums", nums, count)
        ret = []
        for first in range(count - 2):
            print('=====' * 10)
            print("first", first, nums[first])
            if first > 0 and nums[first] == nums[first - 1]:
                print("first", first, "nums[first]", nums[first], "nums[first-1]", nums[first - 1], "continue")
                continue
            target = 0 - nums[first]
            print('target', target)
            third = count - 1
            for second in range(first + 1, count - 1):
                print("second", second, nums[second])
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ret.append([nums[first], nums[second], nums[third]])

        return ret

    def twoSum(self, nums: List[int], target=0) -> List[List[int]]:
        tmp = dict()
        ret = []
        for i, num in enumerate(nums):
            if num in tmp:
                ret.append([tmp[num], i])
            else:
                tmp[target - num] = i
        return ret


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 1, 1]
    # nums = [0, 0, 0]
    s = Solution()
    print(s.threeSum(nums))
