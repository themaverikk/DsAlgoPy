def printFirstNegativeInteger(arr, k):
    firstNegativeIndex = 0

    for i in range(k - 1, len(arr)):

        # skip out of window and positive elements
        while firstNegativeIndex < i and (firstNegativeIndex <= i - k or arr[firstNegativeIndex] > 0):
            firstNegativeIndex += 1

        # check if a negative element is found, otherwise use 0
        firstNegativeElement = arr[firstNegativeIndex] if arr[firstNegativeIndex] < 0 else 0
        print(firstNegativeElement, end=' ')


if __name__ == "__main__":
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    printFirstNegativeInteger(arr, k)

# contributed by Arjun Lather
