"""Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
    Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
    Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string"""

class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation."

a = input("Enter the first number (a): ")
b = input("Enter the second number (b): ")
operation = input("Enter the operation (addition, subtraction, multiplication, division): ")

calculator = Calculator(a, b, operation)
result = calculator.calculate()
print(f"The result of {operation} is: {result}")


"""Example Usage
  Enter the first number (a): 5
  Enter the second number (b): 9
  Enter the operation (addition, subtraction, multiplication, division): addition
  The result of addition is: 14.0  """