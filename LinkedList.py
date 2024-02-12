from collections.abc import Iterable

class Node: 
    """A mutable node class with a value a pointer to another value"""
    def __init__(self, value, pointer=None) -> None:
        self.value = value 
        self.pointer =pointer
    def __str__(self):
        """Returns a string reprenstaion of said node. Recursive method in nature"""
        return f"|{self.value}| -> {self.pointer}"
    
class ssl:
    """Singly linked lists class"""
    def __init__(self, param=None) -> None:
        self.head = None
        self.tail = None 
        if isinstance(param, Iterable):
            for i in param:
                self.append(i) 
        elif param:
            self.push(param)

    def __str__(self) -> str:
        """Returns a string represnation of the linked list"""
        if self._isEmpty():
            return "||"
        return str(self.head)
    
    def __iter__(self):
        """Yields all of the values within the linked list"""
        start = self.head
        while start:
            yield start.value
            start = start.pointer
    
    def __add__(self, other):
        Internal_list = ssl(self)
        if isinstance(other, ssl):
            Internal_list.tail.pointer = other.head
            return Internal_list
        else:
            raise TypeError (f"Can only concatenate ssl with ssl (not {type(other)}) to ssl ")

    def removeAt(self, index:int):
        """Removes a Node at a given index"""
        length = len(self)
        if index>length or index<0:
            raise IndexError(f"Index:{index} is out of bounds")
        if length ==1:
            return self.clear()
        previous = self.head
        start = self.head.pointer
        for i in range (index-1):
            previous, start = start, start.pointer
        previous.pointer = start.pointer

    def popAt(self, index:int):
        """Removes a value at a given index then returns said value"""
        length = len(self)
        if index>=length or index<0:
            raise IndexError(f"Index:{index} is out of bounds")
        previous = self.head
        start = self.head.pointer
        if length ==1:
            removed_val = previous.value
            self.clear()
            return removed_val
        for i in range (index-1):
            previous, start = start, start.pointer
        removed_val = previous.value
        previous.pointer = start.pointer
        return removed_val
    
    def index(self, value):
        if self._isEmpty():
            raise ValueError(f"{value} is not in linked list")
        start = self.head
        count = 0
        if start.value == value:
            return count
        elif self.tail.value == value:
            return len(self)-1
        else:
            while start.value != value and start.pointer != None:
                count+=1
                start= start.pointer
            if count == 0 or count== len(self)-1:
                raise ValueError(f"{value} is not in linked list")
            return count

    def __getitem__(self, index):
        """Gets a item based on its index within the linked list, 
        Supports slicing but not negative indexs. Recursive method"""
        if isinstance(index, int):
            if self._isInRange(index):
                start =self.head
                for i in range(index):
                    start = start.pointer
                return start.value
            else: 
                raise IndexError(f"Index:{index} is out of bounds")
            
        elif isinstance(index, slice):
            sliced_ssl = ssl()
            for i in range(index.stop-1, index.start, -1):
                sliced_ssl.push(self[i])
            sliced_ssl.push(self[index.start])
            return sliced_ssl
        
    def __len__(self) -> int:
        """Returns the length of the linked list"""
        length = 0 
        for i in self:
            length+=1
        return length
    
    def push(self, value):
        """Pushes a value to the front of the list"""
        if self._isEmpty():
            self.head = self.tail = Node(value,self.head)
        else:
            self.head = Node(value,self.head)

    def reverse(self) ->None:
        """Reverses the order of the list"""
        reversed_ssl = ssl()
        for value in self: 
            reversed_ssl.push(value)
        self.head = reversed_ssl.head

    def append(self, value) -> None:
        """Appends a value to the tail end of the linked list"""
        if self._isEmpty():
            self.tail= self.head = Node(value,self.head)
        else:
            self.tail.pointer = Node(value)
            self.tail = self.tail.pointer

    def clear(self) ->None:
        """Clears the linked list"""
        self.head = None
        self.tail = None

    def _isEmpty(self) -> bool:
        """ Internal method of the linked list.\n
        Returns a boolean value based on whether the list is empty or not"""  
        return self.head==None
    
    def _isInRange(self, value)->bool:
        """Interal method of the class linked list.\n
        Returns true if the value passed is within the range of the linked list, else returns false"""
        if value in range (0, len(self)):
            return True
        return False
    
if __name__ == "__main__":
    print(ssl("HelloWorld :)"))

