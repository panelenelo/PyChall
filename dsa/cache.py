from icecream import ic
from collections import deque


class Cache:
    def __init__(self):
        self.elements = []

    def insert(self, value):
        self.elements.append(value)
        if(len(self.elements) > 4):
            print("Cache storage limit reached. Popping the cache")
            self.pop()
        ic(self.elements)

    def pop(self):
        self.elements.pop(0)

    
# Implement the same thing now using collections,
# in this case, using deque
class CacheDeque:
    def __init__(self, len):
        self.deque = deque(maxlen=len)

    def insert(self, value):
        self.deque.append(value)
        ic(self.deque)
        
    def pop(self):
        self.deque.pop()
        ic(self.deque)


def main():
    cache = CacheDeque(3)
    cache.insert(4)
    cache.insert(3)
    cache.insert(2)
    cache.insert(6)
    cache.insert(412)
    cache.insert(44)
    cache.insert(47)

    









if __name__ == "__main__":
    main()