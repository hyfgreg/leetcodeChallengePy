"""
39. 组合总和
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。

对于给定的输入，保证和为 target 的唯一组合数少于 150 个。



示例 1：

输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
示例 4：

输入: candidates = [1], target = 1
输出: [[1]]
示例 5：

输入: candidates = [1], target = 2
输出: [[1,1]]


提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
通过次数318,825提交次数438,569

tag: 数组 回溯
背诵 剪枝技巧

这里的难点在于”剪枝“
因为要求唯一的结果，直接dfs的话，是会有重复的答案被加入的[1,2] [2,1]就是重复的答案
target 3  candidates [1,2,3]

画个图比较好理解
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combination(candidates, target)

    def combination(self, candidates: List[int], target, begin=0) -> List[List[int]]:
        ret = []
        for idx, c in enumerate(candidates[begin:]):
            new_target = target - c
            if new_target == 0:
                ret.append([c])
            elif new_target > 0:
                sub_ret = self.combination(candidates, new_target, idx + begin)
                for sub in sub_ret:
                    tmp = sub[:]
                    tmp.append(c)
                    ret.append(tmp)
        return ret


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(s.combinationSum(candidates, target))
    candidates = [2, 3, 5]
    target = 8
    print(s.combinationSum(candidates, target))
    candidates = [2]
    target = 1
    print(s.combinationSum(candidates, target))
    candidates = [1]
    target = 1
    print(s.combinationSum(candidates, target))
    candidates = [1]
    target = 2
    print(s.combinationSum(candidates, target))
