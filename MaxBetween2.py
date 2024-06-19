# Program to find the maximum between two numbers.
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    if number1 > number2:
        maximum_number = number1
    else:
        maximum_number = number2

    print(f"The maximum between {number1} and {number2} is: {maximum_number}")

except ValueError:
    print("Error: Please enter valid numeric values.")
