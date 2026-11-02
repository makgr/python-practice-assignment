# Problem 2: Student Grade Calculator

name = input("Enter student name: ")
m1 = float(input("Enter Math marks: "))
m2 = float(input("Enter English marks: "))
m3 = float(input("Enter Python marks: "))

# Validate mark boundaries (0 to 100)
if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
    avg = (m1 + m2 + m3) / 3

    if avg >= 80:
        grade = "A+"
    elif avg >= 70:
        grade = "A"
    elif avg >= 60:
        grade = "A-"
    elif avg >= 50:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "F"

    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Final Grade: {grade}")