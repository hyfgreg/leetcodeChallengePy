"""139. 单词拆分
中等
相关标签
premium lock icon
相关企业
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。



示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false


提示：

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅由小写英文字母组成
wordDict 中的所有字符串 互不相同

面试中遇到过这道题?
1/5
是
否
通过次数
1,018,346/1.7M
通过率
60.1%
相关标签
字典树
记忆化
数组
哈希表
字符串
动态规划
"""

from typing import List


class Solution:
    def wordBreakDFS(self, s: str, wordDict: List[str]) -> bool:
        """
        他妈的，会超时
        """
        if not s:
            return False
        if not wordDict:
            return False

        for word in wordDict:
            if s == word:
                return True
            if s.startswith(word):
                ans = self.wordBreak(s[len(word) :], wordDict)
                if ans:
                    return True

        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        if not wordDict:
            return False
        dp = [False] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and (
                    (s[i - len(word) : i] == word and dp[i - len(word)])
                    or s[:i] == word
                ):
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    solu = Solution()
    print(solu.wordBreak(s, wordDict))
