
def kelements(nums, k):
        map = {}
        map2 = {}
        output = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1
        for i,j in map.items():
             print(i)
             print(j)
             map2[i] = j
        print(map2)
        # for key,value in map.items():
        #     map2[value] = key
        #     print(f"map2[{value}] = {key}")
        Sort = list(map2.keys())
        Sort.sort(reverse=True)

        map = {map2[i]: i for i in Sort}

        

        for _ in range(k):
            output.append(map2[Sort[_]])
        return output

def main(args=None):
    nums = [1,2]
    k = 2
    output = kelements(nums, k)

    print(output)

if __name__ == '__main__':
    main()
        