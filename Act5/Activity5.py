def divide(a, b):
    if b == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return a % b

def summation(start, end):
    if start > end:
        print("Error: The second number must be greater than the first.")
        return None
    return sum(range(start, end + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Input your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Goodbye!")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                
                if choice == 'D':
                    result = divide(num1, num2)
                elif choice == 'E':
                    result = exponentiation(num1, num2)
                elif choice == 'R':
                    result = remainder(num1, num2)
                elif choice == 'F':
                    result = summation(num1, num2)
                
                if result is not None:
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
