class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None   # head is top

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node  

    # Pop operation
    def pop(self):
        if self.top is None:
            return None   # underflow
        value = self.top.data
        self.top = self.top.next
        return value

    # Peek operation
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    # Check empty
    def is_empty(self):
        return self.top is None 
    

def is_valid(expression):
    stack = Stack()

    for ch in expression:
        # Opening brackets
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)

        # Closing brackets
        elif ch == ')' or ch == '}' or ch == ']':
            if stack.is_empty():
                return False   # mismatch

            top = stack.pop()

            # Matching check
            if (ch == ')' and top != '(') or \
               (ch == '}' and top != '{') or \
               (ch == ']' and top != '['):
                return False

    # If stack empty → valid
    return stack.is_empty()  



test_cases = ["()", "([])", "([)]", "{[()]}", "(", ""]

for s in test_cases:
    print(s, "->", is_valid(s))    









