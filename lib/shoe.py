#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"
    
    # getter metod
    @property
    def size(self):
        return self._size
    
    # setter method
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else: 
           print("size must be an integer") 
        
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    pass

jordan = Shoe("jordan", 43)
print(jordan.brand)
print(jordan.size)
jordan.size = 35.90
