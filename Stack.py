# Danna Karina Gonzalez Valencia - A00833606

# Stack
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    #Push
    def push(self, x):
        self.stack.append(x)
    
    #Pop
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    #Peek (last element)
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def __str__(self):
        return f"Stack: {self.stack}"
