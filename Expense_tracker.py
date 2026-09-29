import json
import os


FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Enter your expense: ")

    try:
        amount = float(input("Enter the amount of your expense: "))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses(expenses):

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\n===== YOUR EXPENSES =====")

    for item in expenses:
        print(f"{item['name']} - Rs. {item['amount']}")


def view_summary(expenses):

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    total = 0

    for item in expenses:
        total += item["amount"]

    print("\n===== SUMMARY =====")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total expenses: Rs. {total}")


expenses = load_expenses()

running = True

while running:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        view_summary(expenses)

    elif choice == "4":
        print("Exiting...")
        running = False

    else:
        print("Invalid Choice")