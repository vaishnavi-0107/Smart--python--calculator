def smart_calculator():
    print("Smart Calculator")
    print("Type a math expression like 8+5, 12/4, or 7 * 3")

    expression = input("Enter your expression: ")

    try:
        result = eval(expression)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("Invalid expression. Please enter a valid math operation.")

# Run the calculator
smart_calculator()
