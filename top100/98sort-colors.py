"""75. 颜色分类
中等
相关标签
premium lock icon
相关企业
提示
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。



示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]


提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2


进阶：

你能想出一个仅使用常数空间的一趟扫描算法吗？

面试中遇到过这道题?
1/5
是
否
通过次数
950,220/1.5M
通过率
63.6%
相关标签
数组
双指针
排序
"""

from typing import List

"""
问题分析
这是一个典型的 荷兰国旗问题（Dutch National Flag Problem），由 Edsger Dijkstra 提出。核心思想是使用三个指针：

p0：指向下一个 0 应该放置的位置（左边界）

p2：指向下一个 2 应该放置的位置（右边界）

curr：当前遍历的位置

我们遍历数组，根据 nums[curr] 的值：

若为 0，则与 p0 交换，然后 p0++、curr++（因为交换过来的数一定是之前处理过的 1，可以继续前进）

若为 2，则与 p2 交换，然后 p2--（但 curr 不动，因为交换过来的数可能是 0 或 1，需要重新检查）

若为 1，则 curr++

当 curr > p2 时停止，所有元素都已分类。
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0, curr, p2 = 0, 0, len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
                # p0要么指着0，要么指着1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1  # 这里只操作p2，因为交换过来的数字，如果是0，即交换后nums[curr]==0, 需要在下一次迭代中，继续尝试把0往前面移动
            else:  # nums[curr] == 1
                curr += 1


if __name__ == "__main__":
    nums = [2, 1, 0, 2, 1, 1, 1, 0]
    # nums = [2, 0, 1]
    solu = Solution()
    solu.sortColors(nums)
    print(nums)
