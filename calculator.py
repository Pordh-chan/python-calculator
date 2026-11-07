class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


    def multiply(self, a, b):
        result = 0
        for i in range(b+1):
            result = self.add(result, a)
        return result

    # กรณี b เป็นลบ
    def multiply(self, a, b):
        result = 0
        pos_b = b if b >= 0 else self.subtract(0, b)
        for i in range(pos_b):
            result = self.add(result, a)
        return result if b >= 0 else self.subtract(0, result)


    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        same_sign = (a >= 0 and b >= 0) or (a < 0 and b < 0)
        pos_a = a if a >= 0 else self.subtract(0, a)
        pos_b = b if b >= 0 else self.subtract(0, b)
        result = 0
        while pos_a >= pos_b:
            pos_a = self.subtract(pos_a, pos_b)
            result += 1
        return result if same_sign else self.subtract(0, result)
    
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        pos_a = a if a >= 0 else self.subtract(0, a)
        pos_b = b if b >= 0 else self.subtract(0, b)
        while pos_a >= pos_b:
            pos_a = self.subtract(pos_a, pos_b)
        return pos_a if a >= 0 else self.subtract(0, pos_a)
    

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
            
        # หาเครื่องหมายของผลลัพธ์
        same_sign = (a >= 0 and b >= 0) or (a < 0 and b < 0)
        
        pos_a = a if a >= 0 else self.subtract(0, a)
        pos_b = b if b >= 0 else self.subtract(0, b)
        
        result = 0
        while pos_a >= pos_b:
            pos_a = self.subtract(pos_a, pos_b)
            result += 1
            
        return result if same_sign else self.subtract(0, result)

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
            
        pos_a = a if a >= 0 else self.subtract(0, a)
        pos_b = b if b >= 0 else self.subtract(0, b)
        
        while pos_a >= pos_b:
            pos_a = self.subtract(pos_a, pos_b)
            
        return pos_a if a >= 0 else self.subtract(0, pos_a)

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))

