# Exchange values using a third variable.
a = 5
b = 10
print(f"Before exchange: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"After exchange (using third variable): a = {a}, b = {b}")

# Exchange values without using a third variable
a = 5
b = 10
print(f"Before exchange: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After exchange (without using third variable): a = {a}, b = {b}")
