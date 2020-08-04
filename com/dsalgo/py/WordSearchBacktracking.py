from typing import List


def is_valid(board, i, j, visited):
    return 0 <= i < len(board) and 0 <= j < len(board[0]) and not visited[i][j]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        possible_words = set()
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        words_dict = set(words)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.findWordsWithCurrent(board, i, j, "", words_dict, visited, possible_words)

        return list(possible_words)

    def findWordsWithCurrent(self, board, i, j, processing_word, words_dict, visited, possible_words):
        visited[i][j] = True

        curr_word = processing_word + board[i][j]
        if curr_word in words_dict:
            possible_words.add(curr_word)

        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        for idx in range(len(x)):
            next_i = i + x[idx]
            next_j = j + y[idx]

            if is_valid(board, next_i, next_j, visited):
                self.findWordsWithCurrent(board, next_i, next_j, curr_word, words_dict, visited, possible_words)

        visited[i][j] = False


if __name__ == "__main__":
    s = Solution()

    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]

    print(s.findWords(board, words))
