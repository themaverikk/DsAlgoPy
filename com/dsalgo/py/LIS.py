def lis(arr):
    longest = []

    for e in arr:
        included = False

        for i in range(len(longest) - 1, -1, -1):
            if e > longest[i][-1]:
                included = True
                new_seq = longest[i].copy()
                new_seq.append(e)

                if i == len(longest) - 1:
                    longest.append(new_seq)
                else:
                    longest[i + 1] = new_seq

                break

        if not included:
            if longest:
                longest[0] = [e]
            else:
                longest.insert(0, [e])

    return longest[-1]


print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
