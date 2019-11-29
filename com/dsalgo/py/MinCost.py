import sys


def minCost(arr):
    dp = [[0] * len(arr[0]) for _ in range(len(arr))]

    return min_cost(arr, dp, 0, 0)


if __name__ == '__main__':
    arr = [[-2, -3, 3],
           [-5, -10, 1],
           [10, 30, -5]]

    print(minCost(arr))


def min_cost(arr, dp, i, j):
    if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
        return sys.maxsize

    if i == len(arr) - 1 and j == len(arr[0]) - 1:
        return 1 if arr[i][j] >= 0 else 1 - arr[i][j]

    min_cost_next = min(min_cost(arr, dp, i + 1, j), min_cost(arr, dp, i, j + 1))

    return 1 if arr[i][j] - min_cost_next >= 0 else -(arr[i][j] - min_cost_next)
