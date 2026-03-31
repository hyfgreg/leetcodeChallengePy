"""17. 电话号码的字母组合
中等
相关标签
premium lock icon
相关企业
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。





示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = "2"
输出：["a","b","c"]


提示：

1 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

面试中遇到过这道题?
1/5
是
否
通过次数
1,319,290/2.1M
通过率
63.4%
相关标签
哈希表
字符串
回溯
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        ret = []
        tmp = []

        def dfs(i):
            if i >= len(digits):
                ret.append("".join(tmp))
                return
            d = digits[i]
            for ch in digits_letters[d]:
                tmp.append(ch)
                dfs(i + 1)
                tmp.pop()

        dfs(0)
        return ret
    
if __name__ == "__main__":
    digits = "23"
    digits = "2"
    solu = Solution()
    print(solu.letterCombinations(digits))
