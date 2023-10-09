def maxdotproduct(nums, target):
    output = [-1, -1]
    
    if target in nums:
        a = nums.index(target)
        output[0] = a
        nums[nums.index(target)] = -12345678
        nums.index(target)
        while target in nums:
            output[1] = nums.index(target)
            nums[nums.index(target)] = -12345678
    else:
        output.append(a)
    return output

def main(args=None):
    nums = [5,7,7,8,8,8,10]
    target = 8

    output = maxdotproduct(nums, target)

    print(output)

if __name__ == '__main__':
    main()