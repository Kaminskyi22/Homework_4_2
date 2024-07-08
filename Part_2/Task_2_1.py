expression = input("Enter an arithmetic expression (e.g., 23 + 12): ")

expression = expression.replace(' ', '')

operators = ['+', '-', '*', '/']


operator = ''
for char in expression:
    if char in operators:
        operator = char
        break


if operator:
    parts = expression.split(operator)
    if len(parts) == 2:
        try:
       
            numbers = [float(parts[0]), float(parts[1])]

            if operator == '+':
                result = numbers[0] + numbers[1]
            elif operator == '-':
                result = numbers[0] - numbers[1]
            elif operator == '*':
                result = numbers[0] * numbers[1]
            elif operator == '/':
                if numbers[1] == 0:
                    print("Error: division by zero.")
                else:
                    result = numbers[0] / numbers[1]
            else:
                print("Invalid operator. Available operators: +, -, *, /.")
            
            if operator in ['+', '-', '*', '/'] and not (operator == '/' and numbers[1] == 0):
                print("Result:", result)
        except ValueError:
            print("Invalid number format. Please enter valid numbers.")
    else:
        print("Invalid expression format. Please enter the expression in the format: number operator number")
else:
    print("Operator not found. Available operators: +, -, *, /.")
