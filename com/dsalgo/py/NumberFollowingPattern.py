def count(s, ch, i):
    count = 0

    idx = i

    while idx < len(s) and s[idx] == ch:
        count += 1
        idx += 1

    return count


def min_number(s):
    if len(s) < 1:
        return ""

    min_str = ""

    if s[0] == "I":
        min_str += "1"
        lp = mp = 1

    else:
        count_d = count(s, "D", 0)
        min_str += str(count_d + 1)
        lp = mp = count_d + 1

    i = 0
    while i < len(s) - 1:
        if s[i] == 'I':
            while i < len(s) - 1 and s[i + 1] == 'I':
                lp = mp = mp + 1
                min_str += str(lp)
                i += 1

            if i < len(s) - 1:
                count_d = count(s, 'D', i + 1)
                mp = lp = mp + count_d + 1
                min_str += str(lp)
                i += 1

        else:
            while i < len(s) - 1 and s[i] == 'D':
                lp -= 1
                min_str += str(lp)
                i += 1

    lp = mp + 1 if s[i] == 'I' else lp - 1

    min_str += str(lp)

    return min_str


tests = int(input())

for i in range(tests):
    seq = input()
    print(min_number(seq))
