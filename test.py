from icecream import ic


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

    




def main():
    cache = Cache()
    cache.insert(4)
    cache.insert(3)
    cache.insert(2)
    cache.insert(6)
    cache.insert(412)
    cache.insert(44)
    cache.insert(47)

    









if __name__ == "__main__":
    main()