# Program to find area of rectangle, square and circle.
import math
try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area_rectangle = length * width
    print(f"Area of rectangle: {area_rectangle}")

    side = float(input("Enter the side length of the square: "))
    area_square = side ** 2
    print(f"Area of square: {area_square}")

    radius = float(input("Enter the radius of the circle: "))
    area_circle = math.pi * radius ** 2
    print(f"Area of circle: {area_circle}")

except ValueError:
    print("Error: Please enter valid numeric values.")
