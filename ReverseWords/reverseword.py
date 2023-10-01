
def reverseword(s):
        t = s.split()
        output = ""
        for i in t:
             output = output + i[::-1] + " "
        
        return output[0:-1]

def main(args=None):
    s = "Let's take LeetCode contest"
    output = reverseword(s)

    print(output)

if __name__ == '__main__':
    main()
        