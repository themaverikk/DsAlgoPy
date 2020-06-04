from typing import List


class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for d1, d2 in dislikes:
            graph[d1 - 1].append(d2 - 1)
            graph[d2 - 1].append(d1 - 1)

        colors = [-1] * n

        for v in range(n):
            if colors[v] == -1 and not self.isBiPartite(v, graph, colors):
                return False

        return True

    def isBiPartite(self, src: int, graph: List[List[int]], colors: List[int]) -> bool:
        colors[src] = 0
        q = [src]

        while q:
            u = q.pop()

            for v in graph[u]:
                if v == u or colors[v] == colors[u]:
                    return False

                elif colors[v] == -1:
                    colors[v] = 1 - colors[u]
                    q.append(v)

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
