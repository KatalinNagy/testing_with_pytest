import pandas as ps

class Stack:
    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item

    def print_hello(self):
        print("hello")
