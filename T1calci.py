def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

while True:
    print("Enter 'exit' to exit the calculator!")
    operator = input("Enter the operator (+, -, *, /): ")

    if operator.lower() == "exit":
        print("You're exiting the calculator!")
        break

    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))

    if operator == "+":
        print("Result =", addition(a, b))
    elif operator == "-":
        print("Result =", subtraction(a, b))
    elif operator == "*":
        print("Result =", multiplication(a, b))
    elif operator == "/":
        print("Result =", division(a, b))
    else:
        print("You have entered a wrong operator")
