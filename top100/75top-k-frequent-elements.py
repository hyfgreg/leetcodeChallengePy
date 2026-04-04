"""347. 前 K 个高频元素
中等
相关标签
premium lock icon
相关企业
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。



示例 1：

输入：nums = [1,1,1,2,2,3], k = 2

输出：[1,2]

示例 2：

输入：nums = [1], k = 1

输出：[1]

示例 3：

输入：nums = [1,2,1,2,1,2,3,1,3,2], k = 2

输出：[1,2]



提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的


进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。


面试中遇到过这道题?
1/5
是
否
通过次数
911,870/1.4M
通过率
65.6%
相关标签
数组
哈希表
分治
桶排序
计数
快速选择
排序
堆（优先队列）
"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        h = defaultdict(int)
        for n in nums:
            h[n] += 1
        freq_to_nums = defaultdict(list)

        for num, freq in h.items():
            freq_to_nums[freq].append(num)
        counts = list(freq_to_nums.keys())
        print(freq_to_nums)
        print("before heap", counts)

        def build_heap(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[largest] < nums[left]:
                largest = left

            if right < n and nums[largest] < nums[right]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                print("i", i, nums)
                build_heap(nums, n, largest)

        n = len(counts)
        for i in range(n // 2 - 1, -1, -1):
            build_heap(counts, n, i)

        print("after heap", counts)
        # print("k", k)
        kk = 0
        while kk < k:
            kk += len(freq_to_nums[counts[0]])
            counts[0], counts[n - 1] = counts[n - 1], counts[0]
            print("swap", counts)
            n -= 1
            build_heap(counts, n, 0)
        # print(counts)
        n = len(counts)
        ret = []
        for i in range(n - 1, -1, -1):
            ret.extend(freq_to_nums[counts[i]])
            if len(ret) >= k:
                break
        return ret

    def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        max_count = max(cnt.values())
        buckets = [[] for _ in range(max_count + 1)]

        for num, count in cnt.items():
            buckets[count].append(num)
        ans = []
        for b in buckets[::-1]:
            ans.extend(b)
            if len(ans) >= k:
                break
        return ans


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k = 2
    # nums = [1, 1, 1, 2, 2, 3]
    # k = 2
    nums = [
        5,
        1,
        -1,
        -8,
        -7,
        8,
        -5,
        0,
        1,
        10,
        8,
        0,
        -4,
        3,
        -1,
        -1,
        4,
        -5,
        4,
        -3,
        0,
        2,
        2,
        2,
        4,
        -2,
        -4,
        8,
        -7,
        -7,
        2,
        -8,
        0,
        -8,
        10,
        8,
        -8,
        -2,
        -9,
        4,
        -7,
        6,
        6,
        -1,
        4,
        2,
        8,
        -3,
        5,
        -9,
        -3,
        6,
        -8,
        -5,
        5,
        10,
        2,
        -5,
        -1,
        -5,
        1,
        -3,
        7,
        0,
        8,
        -2,
        -3,
        -1,
        -5,
        4,
        7,
        -9,
        0,
        2,
        10,
        4,
        4,
        -4,
        -1,
        -1,
        6,
        -8,
        -9,
        -1,
        9,
        -9,
        3,
        5,
        1,
        6,
        -1,
        -2,
        4,
        2,
        4,
        -6,
        4,
        4,
        5,
        -5,
    ]
    k = 7
    solu = Solution()

    print(solu.topKFrequentBucket(nums, k))
