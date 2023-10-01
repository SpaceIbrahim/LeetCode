
def reversestring(s):
        
        for i in range(int(len(s)/2)):
             t = s[i]
             
             s[i] = s[len(s)-1-i]
             s[len(s)-1-i] = t

        return s

def main(args=None):
    s = ["f", "A", "T"]
    output = reversestring(s)

    print(output)

if __name__ == '__main__':
    main()
        