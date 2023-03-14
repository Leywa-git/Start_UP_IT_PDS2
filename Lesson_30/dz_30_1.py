class HashTable:
    def __init__(self, length=10):
        self.array = [None] * length

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            raise KeyError()

    def remove(self, key):
        index = self.hash(key)
        if self.array[index] == key:
            self.array[index] = None
        else:
            index = index % len(self.array)
            self.array[index] = None

    def print(self):
        return self.array

ht = HashTable()
ht.add(123, 123)
ht.add(12.3, 12.3)
ht.add("123", "orange")
ht.add(35, "apple")
ht.add("fruit", "banana")
print(ht.get("123"))
print(ht.print())
print(ht.get(35))
ht.remove(35)
print(ht.print())
