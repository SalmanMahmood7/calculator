class Calculator:
    def __init__(self):
        self.history_file = "calculator_history.txt"

    # Function to perform calculation
    def calculate(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        else:
            raise ValueError("Invalid operator. Use +, -, *, or /.")

    # Function to save result to history file
    def save_to_history(self, a, b, operator, result):
        with open(self.history_file, "a") as file:
            file.write(f"{a} {operator} {b} = {result}\n")

    # Function to show calculator history
    def show_history(self):
        try:
            with open(self.history_file, "r") as file:
                print("\n--- Calculator History ---")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No history found.")

    # Function to start the calculator
    def start(self):
        try:
            a = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            b = float(input("Enter second number: "))

            result = self.calculate(a, b, operator)
            print(f"Result: {result}")

            self.save_to_history(a, b, operator, result)

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Math Error: {zde}")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Main execution
if __name__ == "__main__":
    calc = Calculator()

    while True:
        print("\n1. Calculate  2. Show History  3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            calc.start()
        elif choice == '2':
            calc.show_history()
        elif choice == '3':
            print("Allah Hafiz!")
            break
        else:
            print("Invalid choice. Please try again.")
