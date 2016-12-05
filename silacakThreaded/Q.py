class Q:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def isNotEmpty(self):
        return self.items != []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.remove(self.front())

    def size(self):
        return len(self.items)

    def front(self): return self.items[0]