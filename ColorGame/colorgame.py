
def colorgame(colors):
        # A = 0
        # B = 0
        # for i in range(1, len(colors)-1):
        #     # print(colors[i - 1], " ", colors[i], " ", colors[i + 1])
        #     if "AAA" in colors:
        #         p = colors.find("AAA")+1
        #         colors = colors[:p] + colors[p+1:]
        #         A += 1
        #     if "BBB" in colors:
        #         p = colors.find("BBB")+1
        #         colors = colors[:p] + colors[p+1:]
        #         B += 1
        
        A = colors.count("AAA")
        B = colors.count("BBB")
        while A == B:
            if "AAA" not in colors:
             return False
            colors = colors.replace('AAA', 'AA')
            colors = colors.replace('BBB', 'BB')
            A = colors.count("AAA")
            B = colors.count("BBB")
            print(A, " ", B, "       ", colors)

        print(A, " ", B)
        return A > B

def main(args=None):
    s = "AABB"
    output = colorgame(s)

    print(output)

if __name__ == '__main__':
    main()
        