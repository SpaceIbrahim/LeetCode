
def kelements(nums, k):
        map = {}
        frequency = {}
        output = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1
        
        for j in map:
            frequency[map[j]] = []
        
        for j in map:
             frequency[map[j]].append(j)

        sort = list(frequency.keys())
        sort.sort(reverse=True)

        print(sort)

        for i in sort:
             for j in frequency[i]:
                output.append(j)
                if len(output) == k:
                     return output
        return output

def main(args=None):
    nums = [2, 1]
    k = 2
    output = kelements(nums, k)

    print(output)

if __name__ == '__main__':
    main()
        