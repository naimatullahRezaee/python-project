print("Welcome to the calculator!")
while True:
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        continue
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))