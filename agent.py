import math

class AIAgent:
    def __init__(self):
        self.operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y,
            'sqrt': lambda x: math.sqrt(x),
            'power': lambda x, y: math.pow(x, y)
        }

    def calculate(self, operation, *args):
        try:
            if operation not in self.operations:
                raise ValueError("Invalid operation")
            return self.operations[operation](*args)
        except Exception as e:
            return str(e)

def main():
    agent = AIAgent()
    print("AI Agent Calculator")
    print("Available operations: add, subtract, multiply, divide, sqrt, power")
    
    while True:
        try:
            operation = input("Enter operation: ")
            if operation == 'exit':
                break
                
            if operation == 'sqrt':
                num = float(input("Enter number: "))
                result = agent.calculate(operation, num)
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = agent.calculate(operation, num1, num2)
                
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == '__main__':
    main()
