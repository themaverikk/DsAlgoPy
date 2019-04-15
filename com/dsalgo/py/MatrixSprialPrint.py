def print_spiral(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        if top <= bottom and left <= right:
            for i in range(left, right + 1):
                print(matrix[top][i], end=' ')
            top += 1

        if top <= bottom and left <= right:
            for i in range(top, bottom + 1):
                print(matrix[i][right], end=' ')
            right -= 1

        if top <= bottom and left <= right:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=' ')
            bottom -= 1

        if top <= bottom or left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=' ')
            left += 1


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30]]

    print_spiral(matrix)
