def calculate():
    operation = input("Enter operation (add, subtract, multiply, divide): ") 

    operation = operation.lower()
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))   

    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
        
    else:
        return "Error: Unknown operation"
    
result = calculate()
print(f"Result: {result}")







