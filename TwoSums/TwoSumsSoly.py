
def twoSum(nums, target):
        map = {}
        output = []
        for i in range(0, len(nums)):
            sum = target - nums[i]
            if sum in map:
                
                output = [i, map[sum]]
            else:
                map[nums[i]] = i
        return output

def main(args=None):
    nums = [2,7,11,15]
    target = 9
    output = twoSum(nums, target)

    print(output)

if __name__ == '__main__':
    main()
        