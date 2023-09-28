
def isanagram(s, t):
        map  = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in map:
                  map[i] = 1
            else:
                map[i] += 1
        for i in t:
            if i in map:
                map[i] -= 1
        
        for val in map.values():
             if val !=0:
                  return False
        return True

def main(args=None):
    s = "aacc"
    t = "caccc"
    output = isanagram(s, t)

    print(output)

if __name__ == '__main__':
    main()
        