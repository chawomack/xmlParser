from collections import deque

class Stack:

    # Creates a stack based on python's deque data structure
    def __init__(self):
        self.values = deque()
        self.length = 0

    # Removes first item in stack using the deque method popleft()
    def pop(self):
        self.length -= 1
        return self.values.popleft()

    # Adds item to beginning of list using deque method appendleft()
    def push(self, new_val):
        self.length += 1
        return self.values.appendleft(new_val)
