
def kelements(nums, k):
        map = {}
        freq = [ [ 0 for i in range(len(nums)) ] for j in range(len(nums)) ]
        output = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1
        
        for k in map:
             freq[map[k]] = k

        print(freq)
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
        