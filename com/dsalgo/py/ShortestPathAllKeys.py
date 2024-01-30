from collections import defaultdict, deque
from typing import List


def isKey(e):
    return 'a' <= e <= 'z'


def hasKey(e, keyMap):
    return 'A' <= e <= 'Z' and keyMap & (1 << (ord(e) - ord('A')))


def neighbors(grid, i, j, keyMap):
    dir = [0, 1, 0, -1, 0]
    neighbors = []

    for k in range(4):
        x, y = i + dir[k], j + dir[k + 1]

        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y] == '.' or grid[x][y] == '@' or isKey(grid[x][y]) or hasKey(grid[x][y], keyMap):
                neighbors.append((x, y))

    return neighbors


def bfs(grid, startingPos, keys):
    q = deque([startingPos])
    visited = defaultdict(set)

    while q:
        i, j, keyMap, steps = q.popleft()

        if isKey(grid[i][j]):
            keyMap |= 1 << (ord(grid[i][j]) - ord('a'))

        if bin(keyMap).count("1") == keys:
            return steps

        if (i, j) not in visited[keyMap]:
            visited[keyMap].add((i, j))

            for x, y in neighbors(grid, i, j, keyMap):
                q.append([x, y, keyMap, steps + 1])

    return -1


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        startingPos = []
        keys = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    startingPos = [i, j, 0, 0]
                elif 'a' <= grid[i][j] <= 'z':
                    keys += 1

        return bfs(grid, startingPos, keys)

s = Solution()
print(s.shortestPathAllKeys(["@...a",".###A","b.BCc"]))