
def colorgame(colors):
        print(colors)
        for i in range(1, len(colors)-1):
            print(colors[i])
        
        return False

def main(args=None):
    s = "AAABABB"
    output = colorgame(s)

    print(output)

if __name__ == '__main__':
    main()
        