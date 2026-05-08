class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = SLLNode(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    def display(self):
        res = []
        temp = self.head
        while temp:
            res.append(temp.data)
            temp = temp.next
        return res  
    

# SLL
sll = SLL()
sll.insert_end(1)
sll.insert_end(2)
print("SLL:", sll.display()) 
 