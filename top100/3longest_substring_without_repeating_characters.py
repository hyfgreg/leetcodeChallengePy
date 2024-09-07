"""
3. 无重复字符的最长子串
中等
相关标签
相关企业
提示
给定一个字符串 s ，请你找出其中不含有重复字符的 最长
子串
 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

"""
//外层循环扩展右边界，内层循环扩展左边界
for (int l = 0, r = 0 ; r < n ; r++) {
	//当前考虑的元素
	while (l <= r && check()) {//区间[left,right]不符合题意
        //扩展左边界
    }
    //区间[left,right]符合题意，统计相关信息
}
外面是右边界
里面是左边界
"""


class Solution:
    def lengthOfLongestSubstringMy(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        left = 0
        right = 1
        val = 0
        ch_index = dict()
        index_ch = dict()
        length = len(s)
        left_ch = s[left]
        ch_index[left_ch] = left
        index_ch[left] = left_ch
        while right < length:
            # print("left", left, "right", right, ch_index, index_ch, val)
            right_ch = s[right]
            if right_ch in ch_index:
                val = max(val, right - left)
                left = ch_index[right_ch] + 1
                i = ch_index[right_ch]
                while i in index_ch:
                    # print("i", i, ch_index, index_ch)
                    a = index_ch.pop(i)
                    i = ch_index.pop(a)
                    i -= 1
            ch_index[right_ch] = right
            index_ch[right] = right_ch
            right += 1
        else:
            # print("left", left, "right", right, ch_index, index_ch, val)
            val = max(val, right - left)
        return val

    def lengthOfLongestSubstring(self, s: str) -> int:
        count = len(s)
        if count < 2:
            return count
        val = 0
        cur_val = 0
        left = 0
        lookup = set()
        for i in range(count):
            # 如果s[i]已经在子串里了，删除左边的字符，直到s[i]不在里面
            while s[i] in lookup:
                cur_val -= 1
                lookup.remove(s[left])
                left += 1
            cur_val += 1
            val = max(val, cur_val)
            lookup.add(s[i])  # 添加s[i]
        return val


if __name__ == '__main__':
    sl = Solution()
    s = "abcabcbb"
    # s = "bbbbb"
    s = "pwwkew"
    # s = "au"
    # s = "abba"
    print(sl.lengthOfLongestSubstring(s))
