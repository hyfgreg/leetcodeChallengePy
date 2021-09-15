"""
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
通过次数239,656提交次数420,573

tag: 数组 分治 快速选择 排序 堆(优先队列)
背诵，要背的不是这个，是快排，妈的，快排的细节还是很多的
"""
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        print(k, arr)
        if len(arr) == k:
            return arr
        p = self._partition(arr)
        print("p", p)
        print(arr)
        if p + 1 == k:
            print("==", arr)
            return arr[:k]
        elif p + 1 > k:
            return self.getLeastNumbers(arr[:p], k)
        else:
            return arr[:p + 1] + self.getLeastNumbers(arr[p + 1:], k - p - 1)

    def _partition(self, arr: List[int]):
        pivot = 0
        left = 1
        right = len(arr) - 1
        while left <= right:
            # print("left", left, "right", right)
            while left < len(arr) and arr[left] <= arr[pivot]:
                left += 1
            while right > 0 and arr[right] > arr[pivot]:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        arr[right], arr[pivot] = arr[pivot], arr[right]
        return right


if __name__ == '__main__':
    s = Solution()
    # arr = [1, 2, 3, 0]
    # k = 2
    # print(s.getLeastNumbers(arr, k))
    # arr = [0, 1, 2, 1]
    # k = 1
    # print(s.getLeastNumbers(arr, k))
    # arr = [0, 0, 0, 2, 0, 5]
    # k = 0
    # print(s.getLeastNumbers(arr, k))
    arr = [0, 0, 2, 3, 3, 5, 6, 0, 3, 4, 4, 4, 3, 0, 9, 14, 4, 17, 6, 4, 10, 18, 21, 13, 8, 4, 12, 6, 19, 11, 8, 12, 14,
           7,
           16, 34, 19, 18, 15, 14, 22, 41, 32, 23, 27, 37, 2, 30, 14, 12, 23, 41, 39, 2, 21, 32, 22, 1, 12, 25, 6, 46,
           7, 61,
           13, 64, 54, 56, 29, 41, 51, 2, 9, 65, 17, 28, 34, 41, 1, 62, 23, 14, 60, 14, 22, 17, 67, 86, 81, 45, 78, 9,
           27, 17,
           30, 54, 35, 42, 72, 94]
    k = 21
    print(s.getLeastNumbers(arr, k))

