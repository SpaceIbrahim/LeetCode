
def containsduplicate(nums):
        map = {}

        for i in range(0, len(nums)):
            if nums[i] in map:
                return True
            else:
                map[nums[i]] = i
        
        return False

def main(args=None):
    nums = [1,2,3,1]
    target = 9
    output = containsduplicate(nums)

    print(output)

if __name__ == '__main__':
    main()
        