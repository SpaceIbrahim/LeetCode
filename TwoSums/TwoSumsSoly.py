
def twoSum(nums, target):
    map = {}
    output = []
    for i in range(0, len(nums)):
        
        if (target - nums[i]) in map.values():
            
            output = [i, list(map.values()).index(target - nums[i])]
        else:
            map[i] = nums[i]
    return output

def main(args=None):
    nums = [2,7,11,15]
    target = 9
    output = twoSum(nums, target)

    print(output)

if __name__ == '__main__':
    main()
        