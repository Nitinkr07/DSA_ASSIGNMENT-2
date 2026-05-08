def is_valid(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# Parentheses
print("Valid:", is_valid("(a+b)"))
print("Invalid:", is_valid("(a+b]")) 