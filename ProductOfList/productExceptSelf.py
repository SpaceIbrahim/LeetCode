def productExceptSelf(nums):
    from numpy import prod
    def mulitply(l):
        result = 1
        for x in l:
            result = result * x
        return result

    output = []

    for i in range(len(nums)):
        t = nums[i]
        nums[i] = 1
        output.append(prod(nums))
        nums[i] = t

    return output

def main(args=None):
    nums = [1,2,3,4]
    res = [1] * len(nums)
    # output = productExceptSelf(nums)

    # print(output)

    print(res, " ", nums)
    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    postfix = 1
    print(res)
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    print(res)

if __name__ == '__main__':
    main()
