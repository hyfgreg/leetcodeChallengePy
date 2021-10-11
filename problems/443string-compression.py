"""
443. 压缩字符串
给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。



示例 1：

输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释：
"aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
示例 2：

输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：
没有任何字符串被替代。
示例 3：

输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：
由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
注意每个数字在数组中都有它自己的位置。


提示：

1 <= chars.length <= 2000
chars[i] 可以是小写英文字母、大写英文字母、数字或符号
通过次数56,427提交次数118,242

tag: 双指针 字符串
"""
from typing import List


# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         # chars.sort()
#         count = 1
#         ret = 0
#         curr = chars[0]
#         first_index = 0
#         index = 1
#         while index < len(chars):
#             # print(index, chars, curr, chars[index], count)
#             # if index >= len(chars):
#             #     break
#             ch = chars[index]
#             if curr == ch:
#                 count += 1
#                 index += 1
#             else:
#                 if count == 1:
#                     curr = ch
#                     first_index = index
#                     index += 1
#                 else:
#                     count_len = len(str(count))
#                     pop_count = count - 1 - count_len
#                     index -= pop_count
#                     for sch in str(count):
#                         chars[first_index + 1] = sch
#                         first_index += 1
#                     first_index += 1
#                     while pop_count > 0:
#                         chars.pop(first_index)
#                         # first_index += 1
#                         pop_count -= 1
#                     first_index = index
#                     index += 1
#                     count = 1
#                     curr = ch
#         # print("first_index", first_index, "count", count)
#         if count > 1:
#             count_len = len(str(count))
#             pop_count = count - 1 - count_len
#             index -= pop_count
#             # index += 1
#             for sch in str(count):
#                 chars[first_index + 1] = sch
#                 first_index += 1
#             # print(chars,)
#             first_index += 1
#             while pop_count > 0:
#                 chars.pop(first_index)
#                 # first_index += 1
#                 pop_count -= 1
#         print(chars)
#         return len(chars)


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        n = len(chars)
        count = 1
        for read in range(n):
            if read == n - 1 or chars[read] != chars[read + 1]:
                # print("read", read, "count", count)
                chars[write] = chars[read]
                write += 1
                if count > 1:
                    for ch in str(count):
                        chars[write] = ch
                        write += 1
                    count = 1
            else:
                count += 1
        # print(chars)
        return write


if __name__ == '__main__':
    s = Solution()
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c"]
    print(s.compress(chars))
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(s.compress(chars))
