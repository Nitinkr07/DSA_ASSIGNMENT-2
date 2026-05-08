class DynamicArray:
    def __init__(self):
        self.size = 0          # number of elements
        self.capacity = 1      # initial capacity
        self.array = [None] * self.capacity

    def append(self, value):
        # Resize if needed
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = value
        self.size += 1
        self._print_state("Append")

    def pop(self):
        if self.size == 0:
            print("Array is empty!")
            return None

        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        self._print_state("Pop")
        return value

    def _resize(self, new_capacity):
        print(f" Resizing from {self.capacity} to {new_capacity}")
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def _print_state(self, operation):
        print(f"{operation} -> Size: {self.size}, Capacity: {self.capacity}")  







arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

arr.pop()
arr.pop() 