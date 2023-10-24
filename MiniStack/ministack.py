class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(self.minstack[-1], val))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


def main():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin()) # return -3
    stack.pop()
    print(stack.top()) # return 0
    print(stack.getMin()) # return -2

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()