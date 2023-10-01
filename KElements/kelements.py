
def kelements(nums, k):
        map = {}
        freq = [[] for i in range(nums)+1]
        output = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1
        
        for i in map:
             freq.append(map[i])
        
        freq.sort(reverse=True)
        print(map)

        for _ in range(k):
            output.append(map[freq[_]])
        return output

def main(args=None):
    nums = [2, 1]
    k = 2
    output = kelements(nums, k)

    print(output)

if __name__ == '__main__':
    main()
        