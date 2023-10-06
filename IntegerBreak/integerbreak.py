
def integerbreak(n):
        
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = -float('inf')
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    return dp[n]

def main(args=None):
    int = 10
    output = integerbreak(int)

    print(output)

if __name__ == '__main__':
    main()
        