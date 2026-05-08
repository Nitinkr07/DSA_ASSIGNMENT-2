class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, data):

        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        curr = self.head 

        while curr.next != None:
            curr = curr.next

        curr.next = newnode



    def insertbeginning(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode   


    def display(self):

        curr = self.head

        while curr != None:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")  
        


    def delete(self, key):

        curr = self.head

        if curr and curr.data == key:
            self.head = curr.next
            return

        prev = None

        while curr and curr.data != key:
            prev = curr
            curr = curr.next 

        if curr is None:
            return

        prev.next = curr.next

    def search(self, key):

        curr = self.head

        while curr != None:

            if curr.data == key:
                return True

            curr = curr.next

        return False
    



ll = LinkedList()


ll.insert(20)
ll.insert(30)
ll.insertbeginning(10)
ll.display()  
print(ll.search(50))    