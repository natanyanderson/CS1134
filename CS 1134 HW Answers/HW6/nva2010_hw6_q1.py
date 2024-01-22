from DoublyLinkedList import *
class LinkedQueue:
    def __init__(self):
        self.list = DoublyLinkedList()

    def __len__(self):
        return len(self.list)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, value):
        self.list.add_last(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.list.delete_first()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.list.header.next.data
