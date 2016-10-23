class SinglePointerNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class DoublePointerNode:
    def __init__(self, data, previous, next):
        self.data = data
        self.previous = previous
        self.next = next