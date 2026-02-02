class MyQueue:

    def __init__(self):
        self.queue = []
    def push(self, x: int) -> None:
        self.queue +=[x]

    def pop(self) -> int:
        return_val = self.queue[0]
        del self.queue[0]
        return return_val

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        else: return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
