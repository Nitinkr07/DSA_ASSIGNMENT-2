class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end (helper)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

        print("Inserted", data)
        self.traverse()

    # Insert after a target value
    def insert_after(self, target, x):
        temp = self.head

        while temp is not None:
            if temp.data == target:
                new_node = Node(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next is not None:
                    temp.next.prev = new_node

                temp.next = new_node

                print("Inserted", x, "after", target)
                self.traverse()
                return

            temp = temp.next

        print("Target not found:", target)

    # Delete at position (1-based)
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Delete head
        if pos == 1:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            print("Deleted position", pos)
            self.traverse()
            return

        count = 1
        while temp is not None and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        # Delete middle/tail
        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

        print("Deleted position", pos)
        self.traverse()

    # Traverse forward
    def traverse(self):
        temp = self.head

        if temp is None:
            print("List is Empty")
            return

        print("List:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None") 



dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

dll.insert_after(20, 25)

dll.delete_at_position(1)   # delete head
dll.delete_at_position(2)   # delete middle
dll.delete_at_position(5)   # invalid 