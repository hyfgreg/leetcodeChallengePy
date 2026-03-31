"""78. 子集
中等
相关标签
premium lock icon
相关企业
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

面试中遇到过这道题?
1/5
是
否
通过次数
1,242,815/1.5M
通过率
82.0%
相关标签
位运算
数组
回溯
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ret = []
        tmp = []

        def dfs(depth):
            #print(f">>>>> start depth {depth} >>>>>")
            if depth == len(nums):
                ret.append(tmp[:])
                #print(f"~~~~~ ret {ret} ~~~~~")
                #print(f"<<<< finish depth {depth} <<<<<")
                return
            tmp.append(nums[depth])
            #print(f"----- depth {depth}, tmp {tmp} -----")
            dfs(depth + 1)
            tmp.pop()
            #print(f"----- depth {depth}, tmp {tmp} -----")
            dfs(depth + 1)
            #print(f"<<<< finish depth {depth} <<<<<")

        dfs(0)
        return ret


if __name__ == "__main__":
    nums = [1, 2, 3]
    solu = Solution()
    print(solu.subsets(nums))
