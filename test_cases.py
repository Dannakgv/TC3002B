# Danna Karina Gonzalez Valencia - A00833606

import unittest
from stack import Stack
from queues import Queue
from dictionary import Dictionary

# Test cases de clase Stack
class TestStack(unittest.TestCase):

    #Test 1: Verifica que el stack este vació al crearlo
    def test_stack_starts_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    #Test 2: Verifica inserción y la consulta del último elemento
    def test_push_and_peek(self):
        stack = Stack()
        stack.push(15)
        stack.push(30)
        stack.push(40)
        self.assertEqual(stack.peek(), 40) # Último elemento es 40

    #Test 3: Verifica extracción LIFO
    def test_pop(self):
        stack = Stack()
        stack.push(15)
        stack.push(30)
        value = stack.pop()
        self.assertEqual(value, 30)  # pop debe extraer el último insertado
        self.assertEqual(stack.peek(), 15)  # Último elemento es 15


# Test cases de clase Queue
class TestQueue(unittest.TestCase):

    # Test 4: Verifica que el queue este vacío al crealo
    def test_queue_starts_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

    # Test 5: Verifica inserción y la consulta del primer elemento
    def test_enqueue_and_peek(self):
        queue = Queue()
        queue.enqueue("casa")
        queue.enqueue("perro")
        queue.enqueue("gato")
        self.assertEqual(queue.peek(), "casa")  # El primer elemento debe ser "casa"

    # Test 6: Verifica extracción FIFO
    def test_unqueue(self):
        queue = Queue()
        queue.enqueue("casa")
        queue.enqueue("perro")
        queue.enqueue("gato")
        value = queue.unqueue()
        self.assertEqual(value, "casa") # unqueue debe extraer primero "casa"
        self.assertEqual(queue.peek(), "perro")  # El primer elemento debe ser "perro"


# Test cases de clase Dictionary
class TestDictionary(unittest.TestCase):

    # Test 7: Verifica inserción y obtención de los valores
    def test_insert_and_get(self):
        dic = Dictionary()
        dic.insert("name", "Danna")
        dic.insert("age", 22)
        self.assertEqual(dic.get("name"), "Danna") # Se obtiene la key "name" con el value "Danna"
        self.assertEqual(dic.get("age"), 22) # Se obtiene la key "age" con el value 22

    # Test 8: Verfica que get devuelve un valor por defecto si la key no existe
    def test_get_default(self):
        dic = Dictionary()
        dic.insert("name", "Danna")
        self.assertEqual(dic.get("country", "Does not exist"), "Does not exist")

    # Test 9: Verifica si se contiene o no una clave
    def test_contains(self):
        dic = Dictionary()
        dic.insert("city", "Napoli")
        self.assertTrue(dic.contains("city"))
        self.assertFalse(dic.contains("country"))

    # Test 10: Verifica la eliminación de elementos según su clave
    def test_delete(self):
        dic = Dictionary()
        dic.insert("city", "Napoli")
        dic.delete("city")
        self.assertFalse(dic.contains("city"))

    # Test 11: Verifica que clear vacía el diccionario
    def test_clear(self):
        dic = Dictionary()
        dic.insert("name", "Danna")
        dic.insert("age", 22)
        dic.clear()
        self.assertEqual(len(dic.keys()), 0)


# Ejecutar pruebas
if __name__ == '__main__':
    unittest.main()
