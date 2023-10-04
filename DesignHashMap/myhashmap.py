class MyHashMap(object):

    def __init__(self):
        self.map = []
        self.keys = []

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keys:
            self.map[self.keys.index(key)][1] = value
        else:
            self.keys.append(key)
            self.map.append([key, value])
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keys:
            return -1
        return self.map[self.keys.index(key)][1]

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.keys:
            return
        self.map.remove(self.map[self.keys.index(key)])
        self.keys.remove(key)
        
def main(args=None):
    myHashMap =  MyHashMap()
    myHashMap.put(1, 1)
    myHashMap.put(2, 2)
    myHashMap.get(1)
    myHashMap.get(3)
    myHashMap.put(2, 1)
    myHashMap.get(2)
    myHashMap.remove(2)
    myHashMap.get(2)

    # a = [[2,1],[5,3]]
    # b = [x[0] for x in a]
    # print(a)
    # print(b)

if __name__ == '__main__':
    main()