def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

n = int(input("Enter the number you want to find factorial of : "))
print(f"Factorial of {n} through iteration is {factorial_iterative(n)}")
print(f"Factorial of {n} through recursion is {factorial_recursive(n)}")