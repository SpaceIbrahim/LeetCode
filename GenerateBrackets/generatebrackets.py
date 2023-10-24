def generatebrackets(n :int):
    stack = ["(","("]
    ctack = [")",")"]
    output = []
    for i in range(0,n):
        s = ""
        for j in range(0,n):
            s += stack[j]

    print(output)

    pass


print(generatebrackets(3))