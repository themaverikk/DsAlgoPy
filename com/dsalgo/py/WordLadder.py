from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = {key: beginWord == key for key in wordList}

        if endWord not in wordListSet:
            return 0

        base_char = ord('a')

        queue = [beginWord, None]
        level = 1

        while queue:
            curr_word = queue.pop(0)

            if not curr_word:
                if queue:
                    queue.append(None)
                    level += 1

            else:
                if curr_word == endWord:
                    return level

                for i in range(len(curr_word)):
                    curr_char = ord(curr_word[i])

                    for j in range(1, 26):
                        next_word = curr_word[:i] + chr((curr_char - base_char + j) % 26 + base_char) + curr_word[
                                                                                                        i + 1:]

                        if wordListSet.get(next_word) is False:
                            wordListSet[next_word] = True
                            queue.append(next_word)

        return 0


if __name__ == "__main__":
    s = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "tog", "cog"]

    print(s.ladderLength(beginWord, endWord, wordList))
