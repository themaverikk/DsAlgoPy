def buildLowestNumber(number, n):
    if n >= len(number):
        return 0
    lowest_number = number
    removed_digits = 0
    i = 0

    while removed_digits < n:
        if i == len(lowest_number) - 1:
            lowest_number = lowest_number[:-1]
            removed_digits += 1
            i -= 1  # since the length of the lowest_number decreased, decrease i by 1 to stay on the last digit
        elif int(lowest_number[i]) > int(lowest_number[i + 1]):
            lowest_number = lowest_number[:i] + lowest_number[i + 1:]
            removed_digits += 1
        else:
            i += 1

    return int(lowest_number)


if __name__ == "__main__":
    number = "12345"
    n = 2
    print(buildLowestNumber(number, n))

# contributed by Arjun Lather
