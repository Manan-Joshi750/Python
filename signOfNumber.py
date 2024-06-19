# Program to check number is positive, negative or zero.
try:
    number = float(input("Enter a number: "))
    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print("The number is zero.")

except ValueError:
    print("Error: Please enter a valid numeric value.")
