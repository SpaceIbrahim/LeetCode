def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        print(stack)
        if token not in "+-*/":
            stack.append(int(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            match token:
                case "+":
                    stack.append(num1 + num2)
                case "-":
                    stack.append(num1 - num2)
                case "*":
                    stack.append(num1 * num2)
                case "/":
                    stack.append(int(num2 / num1))
                case _:
                    pass

    return stack.pop()

def main():
    Input = ["4","13","5","/","+"]
    print(evalRPN(Input))

if __name__ == "__main__":
    main()