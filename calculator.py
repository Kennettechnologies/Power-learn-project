# Get user inputs for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation menu
print("\nSelect operation:")
print("1. + (Addition)")
print("2. - (Subtraction)")
print("3. * (Multiplication)")
print("4. / (Division)")
print("5. % (Modulus)")
print("6. // (Floor Division)")

# Get operation choice
operation = input("\nEnter the operation number (1-6): ")

# Validate and perform calculation
try:
    choice = int(operation)
    if choice < 1 or choice > 6:
        raise ValueError("Invalid choice")
    
    operator_map = {
        1: ('+', num1 + num2),
        2: ('-', num1 - num2),
        3: ('*', num1 * num2),
        4: ('/', num1 / num2 if num2 != 0 else None),
        5: ('%', num1 % num2 if num2 != 0 else None),
        6: ('//', num1 // num2 if num2 != 0 else None)
    }

    operator, result = operator_map[choice]
    
    # Handle division by zero cases
    if num2 == 0 and choice in (4, 5, 6):
        print("Error: Division by zero is not allowed.")
    else:
        print(f"\n{num1} {operator} {num2} = {result}")

except (ValueError, KeyError):
    print("Invalid input. Please enter a number between 1 and 6.")