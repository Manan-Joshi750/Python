# Demonstration of arithmetic operators in Python
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    addition_result = num1 + num2
    print(f"Addition: {num1} + {num2} = {addition_result}")

    subtraction_result = num1 - num2
    print(f"Subtraction: {num1} - {num2} = {subtraction_result}")

    multiplication_result = num1 * num2
    print(f"Multiplication: {num1} * {num2} = {multiplication_result}")

    division_result = num1 / num2
    print(f"Division: {num1} / {num2} = {division_result}")

    modulus_result = num1 % num2
    print(f"Modulus: {num1} % {num2} = {modulus_result}")

    exponentiation_result = num1 ** num2
    print(f"Exponentiation: {num1} ** {num2} = {exponentiation_result}")

except ValueError:
    print("Error: Please enter valid numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
