# Node class (IMPORTANT)
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = SLLNode(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if not self.top:
            return "Empty"
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.data if self.top else "Empty"


# Testing
st = Stack()
st.push(100)
st.push(200)

print("Stack Pop:", st.pop())   # 200
print("Top:", st.peek())        # 100