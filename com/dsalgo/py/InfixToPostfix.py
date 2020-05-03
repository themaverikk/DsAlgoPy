def convert(infix):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = []
    postfix = ""

    for i in range(len(infix)):
        ch = infix[i]

        if ch.isalpha():
            postfix += ch
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and precedence[stack[-1]] >= precedence[ch]:
                postfix += stack.pop()

            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix


if __name__ == "__main__":
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    print(convert(exp))
