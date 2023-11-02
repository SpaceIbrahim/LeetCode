def generateParenthesis(n: int) -> list[str]:
    stack = []
    res = []

    def backtrack(numO, numC):
        if numO == numC == n:
            res.append("".join(stack))
            return
        
        if numO < n:
            stack.append("(")
            backtrack(numO + 1, numC)
            stack.pop()
        
        if numC < numO:
            stack.append(")")
            backtrack(numO, numC+1)
            stack.pop()

    backtrack(0, 0)
    print(res)

    return res


print(generateParenthesis(3))