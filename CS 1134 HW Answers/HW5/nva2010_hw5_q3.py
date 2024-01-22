from ArrayStack import *
from ArrayDeque import *

class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()
        self.n = len(self.stack) + len(self.deque)

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def push(self, e):
        if self.is_empty():
            self.stack.push(e)
        else:
            self.deque.enqueue_first(e)
        self.n += 1

    def top(self):
        if self.is_empty():
            raise Exception('MidStack is empty')
        if len(self.deque) == 0:
            return self.stack.top()
        else:
            return self.deque.first()

    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self.deque) == 0:
            self.n -= 1
            return self.stack.pop()
        else:
            self.n -= 1
            return self.deque.dequeue_first()

    def mid_push(self, e):
        if self.is_empty():
            self.n += 1
            self.stack.push(e)
        else:
            while len(self.deque) != (len(self) // 2):
                self.stack.push(self.deque.dequeue_last())
            self.n += 1
            self.stack.push(e)