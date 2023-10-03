
def goodpairs(nums):
        num = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    num +=1
        
        return num

def main(args=None):
    nums = [1,2,3,1,1,3]
    output = goodpairs(nums)

    print(output)

if __name__ == '__main__':
    main()
        