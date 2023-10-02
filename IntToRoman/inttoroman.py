
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
  
            elif pos[i] == 4:
                output = output + "IV"

            else:
                output = output +"".join(['I']*(pos[i]))
        if i == 1:
            if pos[i] == 9:
                output = "XC" + output
            elif pos[i] >= 5:
                output = "L" +"".join(['X']*(pos[i]%5)) + output
  
            elif pos[i] == 4:
                output = "XL" + output

            else:
                output = "".join(['X']*(pos[i])) + output
        if i == 2:
            if pos[i] == 9:
                output = "CM" + output
            elif pos[i] >= 5:
                output = "D" +"".join(['C']*(pos[i]%5)) + output
  
            elif pos[i] == 4:
                output = "CD" + output

            else:
                output = "".join(['C']*(pos[i])) + output
        if i == 3:
            if pos[i] == 9:
                output = "CM" + output
            elif pos[i] >= 5:
                output = "D" +"".join(['C']*(pos[i]%5)) + output
  
            elif pos[i] == 4:
                output = "CD" + output

            else:
                output = "".join(['M']*(pos[i])) + output

    return output

def main(args=None):
    s = 1994

    output = inttoroman(s)

    print(output)

if __name__ == '__main__':
    main()
        