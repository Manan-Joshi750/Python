def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def get_fibonacci_sequence(n):
    sequence = [fibonacci_recursive(i) for i in range(n+1)]
    return sequence

n = int(input("Enter the index value up to which you want to observe the Fibonacci sequence : "))
sequence = get_fibonacci_sequence(n)
print(f"The Fibonacci sequence up to index {n} is {sequence}")
print(f"And the value at index {n} of the Fibonacci sequence is {fibonacci_recursive(n)}")