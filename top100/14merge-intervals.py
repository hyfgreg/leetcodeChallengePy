"""56. 合并区间
中等
相关标签
premium lock icon
相关企业
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。



示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
示例 3：

输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。


提示：

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

面试中遇到过这道题?
1/5
是
否
通过次数
1,479,212/2.8M
通过率
53.3%
相关标签
数组
排序
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        ret = []
        tmp = []
        for it in intervals:
            if not tmp:
                tmp = it
                continue
            if it[0] > tmp[-1]:
                ret.append(tmp)
                tmp = it
            else:
                tmp = [tmp[0], max(tmp[1], it[1])]
        else:
            if tmp:
                ret.append(tmp)
        return ret


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    intervals = [[4, 7], [1, 4]]
    solu = Solution()
    print(solu.merge(intervals))
