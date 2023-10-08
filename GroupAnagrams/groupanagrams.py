
def maxdotproduct(strs):
    map = {}
    output = []
    for i in range(len(strs)):
        if ''.join(sorted(strs[i])) in map:
            map[''.join(sorted(strs[i]))].append(i)
        else:
            map[''.join(sorted(strs[i]))] = [i]
            
    for j in map:
        s = []
        for k in map[j]:
            s.append(strs[k])
        output.append(s)
    return output

def main(args=None):
    strs = ["eat","tea","tan","ate","nat","bat"]

    output = maxdotproduct(strs)

    print(output)

if __name__ == '__main__':
    main()