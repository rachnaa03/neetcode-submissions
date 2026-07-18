class MinStack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, val: int) -> None:
        self.items.append(val)
        
    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items.pop()

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items[-1]

    def getMin(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return min(self.items)
        
