from project_rewrite import min_func, max_func, length, multiply, power, div_mod
import re
import os


def display_menu():
    clear_screen()
    display_program_header()
    print("Please select an option from the menu below:")
    print("1. Minimum of two numbers")
    print("2. Maximum of a list of numbers")
    print("3. Length of a list")
    print("4. Multiply two numbers")
    print("5. Power of a number")
    print("6. Division and Modulus of two numbers")
    print("7. Exit")


def clear_screen():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def display_program_header():
    """Displays the name of this program and its author."""
    decorators = "=" * 20
    print(decorators)
    print("Project Rewrite")
    print("Author: Adrian Mróz")
    print(decorators)


def get_menu_selection():
    """Prompt the user to select an option from the menu and return their selection."""
    while True:
        selection = input("Please select an option: ")
        if selection.isdigit() and 1 <= int(selection) <= 7:
            return selection
        print("Invalid menu selection. Please enter a number from 1 to 7.")


def get_numbers_from_user(prompt):
    """Prompt the user to enter two numbers separated by a space and return the numbers as a tuple."""
    while True:
        numbers_str = input(prompt)
        try:
            x, y = map(int, numbers_str.split())
            return x, y
        except ValueError:
            print("Please enter two valid integers separated by a space.")


def get_values_from_user(prompt):
    """Prompt the user to enter two numbers separated by a space and return the numbers as a tuple."""
    while True:
        try:
            numbers_str = input(prompt)
            values = numbers_str.split(" ")
            if all(is_number(x) for x in values):
                values = [float(x) for x in values]
                return values
            else:
                print("Please enter a list of valid numbers separated by spaces.")
        except ValueError:
            print("Please enter a list of valid numbers separated by spaces.")


def is_number(string):
    """Determine if a string represents a number."""
    return bool(re.match(r"^[+-]?\d+.?\d*$", string))


def main():
    is_running = True
    while is_running:
        display_menu()
        menu_selection = get_menu_selection()
        if menu_selection == "1":
            x, y = get_numbers_from_user("Enter two numbers separated by a space: ")
            print(min_func(x, y))
        elif menu_selection == "2":
            values_list = get_values_from_user("Enter a list of numbers separated by spaces: ")
            print(max_func(values_list))
        elif menu_selection == "3":
            values_list = get_values_from_user("Enter a list of numbers separated by spaces: ")
            print(length(values_list))
        elif menu_selection == "4":
            x, y = get_numbers_from_user("Enter two numbers separated by a space: ")
            print(multiply(x, y))
        elif menu_selection == "5":
            x, y = get_numbers_from_user("Enter two numbers separated by a space: ")
            print(power(x, y))
        elif menu_selection == "6":
            x, y = get_numbers_from_user("Enter two numbers separated by a space: ")
            print(div_mod(x, y))
        elif menu_selection == "7":
            break
        else:
            print("Invalid menu selection. Please enter a number from 1 to 7.")
        is_running = input("Press enter to continue or enter 'q' to exit: ").lower() != "q"


if __name__ == "__main__":
    main()
