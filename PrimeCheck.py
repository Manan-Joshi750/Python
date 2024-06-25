def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  

    sqrt_n = int(n**0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

n = int(input("Enter any number : "))
result = is_prime(n)
if result:
    print(f"{n} is a prime number")
else :
    print(f"{n} is not a prime number")