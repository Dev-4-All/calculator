from typing import ClassVar, Final


class Calculator:
    obj_count = 0

    def __init__(self) -> None:
        calculator = type(self)

        calculator.obj_count += 1

        self.HISTORY_FILE: Final = f"calc_history_{calculator.obj_count}.txt"
        self.history: list[str] = self.load_history()

    def load_history(self) -> list[str]:
        data: list[str] = []

        try:
            with open(self.HISTORY_FILE, "r") as file:
                data = file.readlines()
        except FileNotFoundError:
            pass

        return data

    def show_history(self) -> None:
        if not self.history:
            print("No calculations yet\n")
            return

        print("[Previous calculations]")
        for record in self.history:
            print(record, end="")
        print()

    def save_history(self) -> None:
        with open(self.HISTORY_FILE, "w") as file:
            file.writelines(self.history)

    def calculate(self, choice: str) -> None:
        calculator = type(self)

        a: float = calculator.get_number("Enter first number: ")
        b: float = calculator.get_number("Enter second number: ")

        operator, operation = calculator.operations[choice]

        result: float | None = operation(a, b)
        if result is not None:
            print(f"Result: {result}\n")
            self.history.append(f"{a} {operator} {b} = {result}\n")

    @staticmethod
    def get_number(prompt: str) -> float:
        while True:
            number = input(prompt)
            try:
                return float(number)
            except ValueError:
                print("Please enter a valid number")

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float | None:
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero\n")
            return None

    operations: ClassVar = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }


def display_options() -> None:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show history")
    print("6. Exit")


def main() -> None:
    print("Welcome to Py Calculator!\n")

    calc = Calculator()

    while True:
        display_options()

        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4"]:
            calc.calculate(choice)
        elif choice == "5":
            calc.show_history()
        elif choice == "6":
            calc.save_history()
            print("\nThanks for using our service!")
            break
        else:
            print("Please choose a valid option\n")


if __name__ == "__main__":
    main()
