# Program to find the grade of students. 
try:
    marks = float(input("Enter the marks: "))
    if 90 <= marks <= 100:
        grade = 'S'
    elif 80 <= marks < 90:
        grade = 'A'
    elif 70 <= marks < 80:
        grade = 'B'
    elif 60 <= marks < 70:
        grade = 'C'
    elif 50 <= marks < 60:
        grade = 'D'
    elif 40 <= marks < 50:
        grade = 'E'
    elif 0 <= marks < 40:
        grade = 'F'
    else:
        print("Error: Marks should be between 0 and 100.")
        exit()

    print(f"Grade: {grade}")

except ValueError:
    print("Error: Please enter valid numeric values for marks.")
