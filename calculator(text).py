# Simple Calculator Text based
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Divide")
operator = input("Select an operator: ")

if operator == "1":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("= " + str(int(num1) + int(num2)))
elif operator == "2":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("= " + str(int(num1) - int(num2)))
elif operator == "3":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("= " + str(int(num1) * int(num2)))
elif operator == "4":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("= " + str(int(num1) / int(num2)))