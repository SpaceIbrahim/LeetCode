
def inttoroman(num):
    output = ""
    pos = []

    while num != 0:
        pos.append(num % 10)
        num = num // 10
    print(pos)
    for i in range(len(pos)):
        if i == 0:
            if pos[i] == 9:
                output = output + "IX"
            elif pos[i] >= 5:
                output = output + "V" +"".join(['I']*(pos[i]%5))
  
            elif pos[i] >= 5:
                output = output + "V" +"".join(['I']*(pos[i]%5))

            else:
                output = output +"".join(['I']*(pos[i]))

    return output

def main(args=None):
    s = 8

    output = inttoroman(s)

    print(output)

if __name__ == '__main__':
    main()
        