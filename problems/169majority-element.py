"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2


进阶：

尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
通过次数368,994提交次数555,322

tag: 数组 哈希表 分治 计数 排序

哈希 时间O(N) 空间O(N)
排序 时间O(NlogN) 空间O(1)
Boyer-Moore 投票算法 时间O(N) 空间O(1)
"""
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n_2 = len(nums) // 2
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            if count[n] > n_2:
                return n

    def majorityElementMoore(self, nums: List[int]) -> int:
        """
        摩尔投票法思路
        候选人(cand_num)初始化为nums[0]，票数count初始化为1。
        当遇到与cand_num相同的数，则票数count = count + 1，否则票数count = count - 1。
        当票数count为0时，更换候选人，并将票数count重置为1。
        遍历完数组后，cand_num即为最终答案。

        为何这行得通呢？
        投票法是遇到相同的则票数 + 1，遇到不同的则票数 - 1。
        且“多数元素”的个数> ⌊ n/2 ⌋，其余元素的个数总和<= ⌊ n/2 ⌋。
        因此“多数元素”的个数 - 其余元素的个数总和 的结果 肯定 >= 1。
        这就相当于每个“多数元素”和其他元素 两两相互抵消，抵消到最后肯定还剩余至少1个“多数元素”。

        无论数组是1 2 1 2 1，亦或是1 2 2 1 1，总能得到正确的候选人。

        作者：gfu
        链接：https://leetcode-cn.com/problems/majority-element/solution/3chong-fang-fa-by-gfu-2/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        candidate = None
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            if candidate == n:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    s = Solution()
    print(s.majorityElementMoore(nums))
