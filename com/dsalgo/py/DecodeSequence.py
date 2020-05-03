def decodeSequence(digits, i, dp):
    if i >= len(digits):
        return None

    if dp[i]:
        return dp[i]

    if i == len(digits) - 1:
        return [chr(ord('a') + int(digits[i]) - 1)]

    end = i + 1
    currSequence = []
    currStr = int(digits[i:end])

    while end <= len(digits) and int(currStr) < 27:
        nextSequence = decodeSequence(digits, end, dp)

        if nextSequence:
            for nextStr in nextSequence:
                currSequence.append(chr(ord('a') - 1 + currStr) + nextStr)

        end += 1
        currStr = int(digits[i:end])

    dp[i] = currSequence
    return currSequence


if __name__ == "__main__":
    digits = "1234"
    dp = ["" for _ in range(len(digits))]
    print(decodeSequence(digits, 0, dp))
