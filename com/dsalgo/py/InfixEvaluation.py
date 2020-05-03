def apply_operation(operator, operand1, operand2):
    result = 0

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    else:
        result = operand1 / operand2

    return result


def evaluate(infix):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    operator_stack = []
    operand_stack = []

    i = 0
    while i < len(infix):
        ch = infix[i]
        if ch == " ":
            pass
        elif ch.isnumeric():
            i += 1
            while i < len(infix) and infix[i].isnumeric():
                ch += infix[i]
                i += 1

            i -= 1
            operand_stack.append(int(ch))
        elif ch == "(":
            operator_stack.append(ch)
        elif ch == ")":
            while operator_stack[-1] != "(":
                operator = operator_stack.pop()
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()

                operand_stack.append(apply_operation(operator, operand1, operand2))

            operator_stack.pop()

        else:
            while operator_stack and operator_stack[-1] != "(" and precedence[operator_stack[-1]] >= precedence[ch]:
                operator = operator_stack.pop()
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()

                operand_stack.append(apply_operation(operator, operand1, operand2))

            operator_stack.append(ch)

        i += 1

    while operator_stack:
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()

        operand_stack.append(apply_operation(operator, operand1, operand2))

    return operand_stack[-1]


if __name__ == "__main__":
    print(evaluate("10 + 2 * 6"))
    print(evaluate("100 * 2 + 12"))
    print(evaluate("100 * ( 2 + 12 )"))
    print(evaluate("100 * ( 2 + 12 ) / 14"))
