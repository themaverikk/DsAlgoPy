from typing import List


def isValid(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O'


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        for i in range(len(board[0])):
            self.markLiving(board, 0, i)
            self.markLiving(board, len(board) - 1, i)

        for i in range(len(board)):
            self.markLiving(board, i, 0)
            self.markLiving(board, i, len(board[0]) - 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'O' if board[i][j] == 'S' else 'X'

    def markLiving(self, board, i, j):
        if not isValid(board, i, j):
            return

        board[i][j] = 'S'
        isValid(board, i + 1, j) and self.markLiving(board, i + 1, j)
        isValid(board, i - 1, j) and self.markLiving(board, i - 1, j)
        isValid(board, i, j + 1) and self.markLiving(board, i, j + 1)
        isValid(board, i, j - 1) and self.markLiving(board, i, j - 1)


if __name__ == "__main__":
    s = Solution()

    print(s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
