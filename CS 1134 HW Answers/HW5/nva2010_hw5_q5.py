import copy
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()
    for elem in lst:
        stack.push(elem)
    for i in range(len(stack)):
        new_elem = stack.pop()
        if queue.is_empty():
            queue.enqueue([new_elem])
        else:
            for j in range(len(queue)):
                old_elem = queue.dequeue()
                for k in range(len(old_elem) + 1):
                    new_p = copy.copy(old_elem)
                    new_p.insert(k, new_elem)
                    queue.enqueue(new_p)
    return [queue.dequeue() for i in range(len(queue))]