# Program to find the maximum between three numbers.
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))
    if number1 >= number2 and number1 >= number3:
        maximum_number = number1
    elif number2 >= number1 and number2 >= number3:
        maximum_number = number2
    else:
        maximum_number = number3

    print(f"The maximum among {number1}, {number2}, and {number3} is: {maximum_number}")

except ValueError:
    print("Error: Please enter valid numeric values.")
