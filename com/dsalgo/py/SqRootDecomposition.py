import math


class SqRootDecomposition:
    def __init__(self, arr):
        self.arr = arr
        self.blocks = self._preprocess()

    def _preprocess(self):
        blocks = []
        blockSize = math.floor(math.sqrt(len(arr)))
        blockIndex = -1

        for i in range(len(self.arr)):
            if i % blockSize == 0:
                blocks.append(0)
                blockIndex += 1

            blocks[blockIndex] += arr[i]

        return blocks

    def getSum(self, l, r):
        blockSize = math.floor(math.sqrt(len(arr)))
        sum = 0
        index = l

        while index != 0 and index <= r and index % blockSize != 0:
            sum += self.arr[index]
            index += 1

        blockIndex = index % blockSize

        while index + blockSize <= r:
            sum += self.blocks[blockIndex]
            blockIndex += 1
            index += blockSize

        while index <= r:
            sum += self.arr[index]

        return sum


if __name__ == "__main__":
    arr = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
