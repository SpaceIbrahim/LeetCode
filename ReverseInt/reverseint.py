
def reverseint(x):
        
        num = str(x)
        output = ""

        for i in num:
             output = i + output

        if "-" in output:
            output = output[:len(num)-1]
            output = '-' + output

        output = int(output)
        if output > (2**31-1):
             return 0
        elif output < -(2**31):
             return 0
        return output

def main(args=None):
    int = -123
    output = reverseint(int)

    print(output)

if __name__ == '__main__':
    main()
        