class Value:
    """
    Stores a single scalar value and its gradient 
    """

    def __init__(self, data, _children=()):
        self.data = data
        self._prev = set(_children)
    
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def __add__(self, other):
        """
        Defining the addition operation for Value data types
        a + b => a.__add__(b)
        """

        out = Value(self.data + other.data)
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data)
        return out