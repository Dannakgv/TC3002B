# Danna Karina Gonzalez Valencia - A00833606

# Queue
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    #Enqueue
    def enqueue(self, x):
        self.queue.append(x)
    
    #Unqueue
    def unqueue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    #Peek (first element)
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def __str__(self):
        return f"Queue: {self.queue}"
