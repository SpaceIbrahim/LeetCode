class MyHashMap(object):

    def __init__(self):
        self.map = []

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.map.append([key, value])
        print(self.map)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """


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

if __name__ == '__main__':
    main()