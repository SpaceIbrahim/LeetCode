
def kelements(nums, k):
        map = {}
        numSet = set(nums)
        output = []
        k = 0
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1

        for i in map:
            output[k] = i
            k+=1
        return [1]

def main(args=None):
    nums = [1,1,1,2,2,3]
    k = 2
    output = kelements(nums, k)

    print(output)

if __name__ == '__main__':
    main()
        