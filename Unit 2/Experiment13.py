class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation (O(1))
    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:  # Empty queue
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    # Dequeue operation (O(1))
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return None

        removed = self.front.data
        self.front = self.front.next

        # If queue becomes empty
        if self.front is None:
            self.rear = None

        return removed

    # Get front element
    def get_front(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data

    # Display queue
    def display(self):
        temp = self.front
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result 
    


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.get_front())      # 10

print("Dequeued:", q.dequeue())     # 10
print("Front:", q.get_front())      # 20

print("Queue:", q.display())        # [20, 30]