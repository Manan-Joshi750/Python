#FizzBuzz is a problem which displays Fizz when a number is a multiple of 3 and Buzz if it is a multiple of 5 and FizzBuzz when of both....
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

n = int(input("Enter any number : "))
fizzbuzz(n)