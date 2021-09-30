"""
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。



示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]


提示:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
通过次数201,035提交次数322,540

tag: 数组 回溯
背诵，主要是剪枝的办法，官方的看不懂，但是这个还不错，先排序，然后i>0且candidates[i] == candidates[i-1]时continue就行
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = self.dfs(candidates, target)
        return ret

    def dfs(self, candidates: List[int], target: int):
        if not candidates:
            return []
        ret = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] == target:
                ret.append([candidates[i]])
            else:
                tmp_ret = self.dfs(candidates[i + 1:], target - candidates[i])
                for sub in tmp_ret:
                    ret.append([candidates[i]] + sub[:])
        return ret


if __name__ == '__main__':
    s = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(s.combinationSum2(candidates, target))
