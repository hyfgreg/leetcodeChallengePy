"""46. 全排列
中等
相关标签
premium lock icon
相关企业
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

面试中遇到过这道题?
1/5
是
否
通过次数
1,651,392/2.1M
通过率
80.3%
相关标签
数组
回溯
"""

from typing import List

"""
回溯的模板！！！
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }
    for (选择 : 本层集合中的元素) {
        处理节点;
        backtracking(路径, 选择列表); // 递归
        撤销处理; // 回溯
    }
}
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # print(nums)
        if not nums:
            return [[]]
        ret = []
        for i in range(len(nums)):
            sub = self.permute(nums[0:i] + nums[i + 1 :])
            for s in sub:
                s.insert(0, nums[i])
            ret.extend(sub)
        return ret

    def permute_backtrack(self, nums: List[int]) -> List[List[int]]:
        # print(nums)
        if not nums:
            return []
        res = []

        def backtrack(first=0):
            if first == len(nums):
                res.append(nums[:])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    solu = Solution()
    print(solu.permute_backtrack(nums))
