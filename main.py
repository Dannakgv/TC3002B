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

# Dictionary
class Dictionary:
    def __init__(self):
        self._data = {}
    
    #Insert
    def insert(self, key, value):
        self._data[key] = value

    #Delete
    def delete(self, key):
        if key in self._data:
            del self._data[key]
        else:
            return None
    
    #Clear
    def clear(self):
        self._data.clear()
    
    #Get  
    def get(self, key, default=None):
        return self._data.get(key, default) 
    
    #Keys
    def keys(self):
        return self._data.keys()
    
    #Values
    def values(self):
        return self._data.values()
    
    #Items(key,value)
    def items(self):
        return self._data.items()
    
    #Contains
    def contains(self, key):
        return key in self._data
    
    def __str__(self):
        return str(self._data)

#Prueba
def main():
    print("\n=== PRUEBA DE STACK ===")
    stack = Stack()
    
    print("¿Está vacía?", stack.is_empty())  # True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack después de push:", stack)  # [10, 20, 30]
    print("Peek:", stack.peek())            # 30
    print("Pop:", stack.pop())              # 30
    print("Stack después de pop:", stack)   # [10, 20]

    print("\n=== PRUEBA DE QUEUE ===")
    queue = Queue()

    print("¿Está vacía?", queue.is_empty()) # True
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print("Queue después de enqueue:", queue) # ["A", "B", "C"]
    print("Peek:", queue.peek())               # "A"
    print("Unqueue:", queue.unqueue())         # "A"
    print("Queue después de unqueue:", queue)  # ["B", "C"]

    print("\n=== PRUEBA DE DICTIONARY ===")
    dic = Dictionary()

    dic.insert("name", "Danna")
    dic.insert("age", 22)
    dic.insert("city", "Napoli")
    print("Diccionario inicial:", dic)

    print("Obtener 'age':", dic.get("age"))          # 22
    print("Obtener clave inexistente:", dic.get("country", "No existe"))  # "No existe"
    print("Contiene 'name'?", dic.contains("name"))  # True

    dic.delete("city")
    print("Después de eliminar 'city':", dic)

    dic.clear()
    print("Después de clear:", dic)

if __name__ == "__main__":
    main()