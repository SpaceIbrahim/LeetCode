
def maxdotproduct(nums1, nums2):
    n, m = len(nums1), len(nums2)
    memo = [[float('-inf')] * m for _ in range(n)]
    
    def dp(i, j):
        if i == n or j == m:
            return float('-inf')
        
        if memo[i][j] != float('-inf'):
            return memo[i][j]
        
        memo[i][j] = max(
            nums1[i] * nums2[j] + max(dp(i + 1, j + 1), 0),
            dp(i + 1, j),  
            dp(i, j + 1), 
        )
        
        return memo[i][j]
    
    return dp(0, 0)  

def main(args=None):
    nums1 = [2,1,-2,5]
    nums2 = [3,0,-6]

    output = maxdotproduct(nums1, nums2)

    print(output)

if __name__ == '__main__':
    main()
        