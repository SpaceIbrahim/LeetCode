class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = ['a'] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.list[i]

    def set(self, i: int, n: int) -> None:
        if self.list[i] == 'a':
            self.size += 1
        self.list[i] = n
        

    def pushback(self, n: int) -> None:
        if self.list[-1] != 'a':
            self.resize()

        for i in range(self.capacity):
            if self.list[i] == 'a':
                self.list[i] = n
                self.size += 1
                break

    def popback(self) -> int:
        a = self.list[self.size -1]
        self.list[self.size-1] = 'a'
        self.size -= 1
        return a

    def resize(self) -> None:
        self.list = self.list + ['a']* self.capacity
        self.capacity = self.capacity *2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
def main():
    a = DynamicArray(1)
    a.getSize()
    a.getCapacity()
    a.pushback(1)
    a.getSize()
    a.getCapacity()
    a.pushback(2)
    a.getSize()
    a.getCapacity()
    a.get(1)
    a.set(1, 3) 
    a.get(1)
    a.popback()


if __name__ == "__main__":
    main()