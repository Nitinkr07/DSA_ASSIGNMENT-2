# Node class define karo pehle
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new = SLLNode(data)
        if not self.rear:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if not self.front:
            return "Underflow"
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def get_front(self):
        return self.front.data if self.front else "Empty"


# Testing
q = Queue()
q.enqueue(1)
q.enqueue(2)

print("Queue Dequeue:", q.dequeue())  # 1
print("Front:", q.get_front())        # 2