
def kelements(nums, k):
        map = {}
        freq = [[] for i in range(len(nums)+1)]
        output = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1
        
        for j in map:
            freq[map[j]].append(j)

        print(freq)
        for _ in range(len(freq) -1, 0, -1):
            for n in freq[_]:
                output.append(n)
                if len(output) == k+1:
                    break

        return output

def main(args=None):
    nums = [2, 1]
    k = 2
    output = kelements(nums, k)

    print(output)

if __name__ == '__main__':
    main()
        