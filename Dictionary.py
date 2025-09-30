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
