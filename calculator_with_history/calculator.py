HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found.")
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No history file exists yet.")

def clr_history():
    open(HISTORY_FILE, "w").close()
    print("History Cleared Successfully.")

def save_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use: number operator number")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Divide by zero not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    if result.is_integer():
        result = int(result)

    print(f"The result is: {result}")
    save_history(user_input, result)

def main():
    print("Welcome to Calculator")
    print("Type 'exit' to quit, 'history' to view past, 'clr' to clear history")

    while True:
        user_input = input("Enter your calculation: ")
        if user_input == "exit":
            print("Good bye!")
            return
        elif user_input == "history":
            show_history()
        elif user_input == "clr":
            clr_history()
        else:
            calculate(user_input)

main()
