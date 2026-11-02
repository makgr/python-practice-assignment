# Problem 1: Personal Information & Simple Calculator

name = input("Enter your name: ")
age = input("Enter your age: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

print(f"\nHello, {name}!")
print(f"Your age is {age}.")
print(f"Addition: {int(addition) if addition.is_integer() else addition}")
print(f"Subtraction: {int(subtraction) if subtraction.is_integer() else subtraction}")
print(f"Multiplication: {int(multiplication) if multiplication.is_integer() else multiplication}")
print(f"Division: {division}")