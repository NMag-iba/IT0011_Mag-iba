def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Second number must be greater.")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("-------------------------")
        print("\t  Menu")
        print("-------------------------")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        print("-------------------------")
        choice = input("Enter your choice: ").upper()
        print("-------------------------")
        if choice == 'Q':
            print("Exiting program...")
            print("-------------------------")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = float(input("Enter first number:  "))
                num2 = float(input("Enter second number: "))
                print("-------------------------")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiate(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                result = summation(int(num1), int(num2))
            
            if result is not None:
                print("Result:", result)
        else:
            print("Invalid choice.")
            print("-------------------------")

if __name__ == "__main__":
    main()
