class Stack:
    '''This is a Class docstring'''
    class StackPlate():
        '''This is a Class docstring'''
        def __init__(self, value):
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, item):
        '''This is a method docstring'''
        new_plate = self.StackPlate(item)
        new_plate.next = self._head
        self._head = new_plate
        self._size += 1


    def pop(self):
        '''This is a method docstring'''
        if self._size > 0:
            ret = self._head.value
            self._head = self._head.next
            self._size -= 1
            return ret
        raise IndexError

    def top(self):
        '''This is a method docstring'''
        if self._size > 0:
            return self._head.value
        raise IndexError

    def size(self):
        '''This is a method docstring'''
        return self._size

    def clear(self):
        '''This is a method docstring'''
        self._head = None
        self._size = 0

    def is_empty(self):
        '''This is a method docstring'''
        if self._size == 0:
            return True
        return False

    def __iter__(self):
        return self.gen()

    def gen(self):
        '''This is a method docstring'''
        temp = self._head
        for _ in range(self.size()):
            yield temp.value
            temp = temp.next
