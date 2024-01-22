from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.in_stack = ArrayStack()
        self.out_stack = ArrayStack()
        self._size = 0

    def enqueue(self, item):
        self.in_stack.push(item)
        self._size += 1

    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        if self.out_stack.is_empty():
            raise ValueError('Queue is empty')
        self._size -= 1
        return self.out_stack.pop()

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        if self.out_stack.is_empty():
            raise ValueError('Queue is empty')
        return self.out_stack.top()
