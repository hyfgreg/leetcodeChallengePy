"""
tag: 数组 双指针

给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]


提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

重点在于去重，而且返回的是数值不是index，所以可以先给nums排序，升序排序，然后遇到同样的数字只看第一个，后面的忽略
排序后，双指针
[...i,i+1,i+2,...,n-3,n-2,n-1]
       ↑                   ↑
       L->                <-R
不断增加L和减少R，直到发现L>=R
然后增加i，如果i>0 and nums[i]==nums[i-1]->i++
特殊情况，因为排序了，所以当nums[i]>0的时候，可以直接返回答案，因为已经不存在新的数字组合了
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        # print(nums)
        ret = []
        for i in range(length):
            if nums[i] > 0:
                return ret
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ret.append([nums[i], nums[left], nums[right]])
                    while left < right:
                        if nums[left] != nums[left + 1]:
                            break
                        left += 1
                    while left < right:
                        if nums[right - 1] != nums[right]:
                            break
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ret

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))