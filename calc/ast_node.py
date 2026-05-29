


class NumberNode:
    def __init__(self, value: float):
        self.value = value
        
    
    
    def __repr__(self) -> str:
        return f"NumberNode({self.value})"
        
        
        
class BinaryOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        
        
    
    def __repr__(self) -> str:
        return f"BinaryOpNode({self.left}, '{self.op}', {self.right})"