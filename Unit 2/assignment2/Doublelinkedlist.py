class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = DLLNode(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def display_forward(self):
        res = []
        temp = self.head
        while temp:
            res.append(temp.data)
            temp = temp.next
        return res

    def display_backward(self):
        res = []
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            res.append(temp.data)
            temp = temp.prev
        return res 
    

# DLL
dll = DLL()
dll.insert_end(5)
dll.insert_end(10)
print("DLL Forward:", dll.display_forward())
print("DLL Backward:", dll.display_backward()) 