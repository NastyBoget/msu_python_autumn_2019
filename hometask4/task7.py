from collections import deque
class BinarySearchTree:
    
    def __init__(self, value=None):
        self.value = value
        if not value is None:
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
            
    def append(self, value):
        if not self.value is None:
            if self.value > value:
                self.left.append(value)
            else:
                self.right.append(value)
        else:
            self.value = value
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
            
    def __contains__(self, value):
        while not self.value is None:
            if self.value == value:
                return True
            elif self.value > value:
                return value in self.left
            else:
                return value in self.right
            
    def __iter__(self):
        self.it = deque()
        self.it.append(self)
        return self
    
    def __next__(self):
        if len(self.it):
            next_v = self.it.popleft()
            if (len(self.it) == 0) and next_v.value is None:
                raise StopIteration()
            while((len(self.it) != 0) and next_v.value is None):
                next_v = self.it.popleft()
            if next_v.value is None:
                raise StopIteration()
            self.it.append(next_v.left)
            self.it.append(next_v.right)
            return next_v.value
        else:
            raise StopIteration()
