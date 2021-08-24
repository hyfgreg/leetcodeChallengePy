"""
239. 滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。



示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
示例 3：

输入：nums = [1,-1], k = 1
输出：[1,-1]
示例 4：

输入：nums = [9,11], k = 2
输出：[11]
示例 5：

输入：nums = [4,-2], k = 2
输出：[4]


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
通过次数180,580提交次数363,963

tag: 队列 数组 滑动窗口 单调队列 堆(优先队列)

单调队列，同时又是一个双向队列
求最大值维护一个单调递减队列，先进去的要更大
求最小值维护一个单调递增队列，先进去的要更小

另一个方法是维护一个最大优先队列，在往队列里push数据的时候push一个(index,value)的tuple，记录每个value的index，
然后每次移动窗口，要pop数据的时候，不着急pop，除非队列的最大值是需要被pop的

第一次
"""
from typing import List

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ret = []
        for index, num in enumerate(nums):
            if index < k:
                while q and q[0][1] < num:
                    q.popleft()
                q.appendleft((index, num))
            else:
                ret.append(q[-1][1])
                if index - k == q[-1][0]:
                    q.pop()
                while q and q[0][1] < num:
                    q.popleft()
                q.appendleft((index, num))
            print(index, num, q)
        ret.append(q[-1][1])
        return ret


if __name__ == '__main__':
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    # nums = [1]
    # k = 1
    nums = [7, 2, 4]
    k = 2
    s = Solution()
    print(s.maxSlidingWindow(nums, k))
