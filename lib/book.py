#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        pass
    # getter method
    @property
    def page_count(self):
        return self._page_count
    
    # setter method
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else: 
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    pass

book1 = Book("the river and the source", 64)
print(book1.title)
print(book1.page_count)
book1.page_count = 35
book1.turn_page()

    
        