def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on input.
    
    Parameter:
    num1 = 1st number
    num2 = 2nd number
    operation = add, subtract, multiply, divide

    Returns:
    float (the result of the operation) or string (error message) 
    """
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'multiply':
        return num1 * num2
    
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        
        return num1 / num2
        
    else:
        #If anything other string is inputted.
        return f"Error: '{operation}' is not a valid operation."