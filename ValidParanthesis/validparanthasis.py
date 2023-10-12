def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        elif i == '}' and len(stack) != 0 and stack[-1] == '{':
            stack.pop()
        elif i == ']' and len(stack) != 0 and stack[-1] == '[':
            stack.pop()
        else:
            return False
    
    if len(stack) == 0:
        return True
    else:
        return False


def main():
    s = "()"

    output = isValid(s)

    print(output)


if __name__ == '__main__':
    main()