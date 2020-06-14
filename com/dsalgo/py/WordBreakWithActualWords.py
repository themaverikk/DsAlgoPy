from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDictSet = set(wordDict)
        dp = {}
        return self.wordBreakRec(s, 0, wordDictSet, dp)

    def wordBreakRec(self, s, i, wordDictSet, dp):
        if i in dp:
            return dp[i]

        n = len(s)
        if i < 0 or i >= n:
            return [""]

        curr_words = []
        for j in range(i + 1, n + 1):
            word = s[i:j]

            if word in wordDictSet:
                subsequent_words = self.wordBreakRec(s, j, wordDictSet, dp)
                curr_words.extend(map(lambda x: word + " " + x if x else word, subsequent_words))

        dp[i] = curr_words
        return dp[i]


if __name__ == "__main__":
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

    sol = Solution()
    print(sol.wordBreak(s, wordDict))
