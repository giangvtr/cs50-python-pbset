class Jar:
    def __init__(self, capacity=12):
        self.capacity = int(capacity)
        self.size = 0

    def __str__(self):
        return f"{'🍪'*self.size}"

    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        if self.size >= n:
            self.size -= n
            return self.size
        else:
            raise ValueError("Not enough cookies to eat")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self,capacity):
        try:
            capacity = int(capacity)
        except ValueError:
            print("Invalid capacity")
        self._capacity = capacity

    @size.setter
    def size(self, size):
        if not size <= self.capacity:
            raise ValueError("Exceed jar's capacity")
        self._size = size
