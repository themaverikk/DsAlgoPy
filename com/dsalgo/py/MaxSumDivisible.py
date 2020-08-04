def largestSumDivisible(arr, i):
    if not arr:
        return [0]

    if i < 0 or i >= len(arr):
        return [0]

    sum_without = largestSumDivisible(arr, i + 1)

    sum_with = []

    for s in sum_without:
        sum_with.append(arr[i] + s)

    return sum_without + sum_with


def largestSum(arr):
    sums = largestSumDivisible(arr, 0)

    divisibleSum = 0

    for sum in sums:
        if sum % 3 == 0:
            divisibleSum = max(divisibleSum, sum)

    return divisibleSum


if __name__ == '__main__':
    print(largestSum([1, 2, 3, 4, 4]))
