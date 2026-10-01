import json

FILE_NAME = "expenses.json"


# Load saved data
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add income
def add_income(data):
    amount = float(input("Enter income amount: "))
    description = input("Enter income description: ")

    transaction = {
        "type": "income",
        "amount": amount,
        "description": description
    }

    data.append(transaction)
    save_data(data)

    print("Income added successfully!")


# Add expense
def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")

    transaction = {
        "type": "expense",
        "amount": amount,
        "category": category,
        "description": description
    }

    data.append(transaction)
    save_data(data)

    print("Expense added successfully!")


# View all transactions
def view_transactions(data):

    if len(data) == 0:
        print("No transactions found.")
        return

    print("\n===== ALL TRANSACTIONS =====")

    for transaction in data:

        if transaction["type"] == "income":
            print(
                "Income:",
                transaction["amount"],
                "|",
                transaction["description"]
            )

        else:
            print(
                "Expense:",
                transaction["amount"],
                "| Category:",
                transaction["category"],
                "|",
                transaction["description"]
            )


# View summary
def view_summary(data):

    total_income = 0
    total_expenses = 0
    expense_count = 0

    categories = {}

    for transaction in data:

        if transaction["type"] == "income":

            total_income += transaction["amount"]

        else:

            total_expenses += transaction["amount"]
            expense_count += 1

            category = transaction["category"]

            if category in categories:
                categories[category] += transaction["amount"]
            else:
                categories[category] = transaction["amount"]

    balance = total_income - total_expenses

    print("\n===== FINANCIAL SUMMARY =====")

    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Number of Expenses:", expense_count)
    print("Remaining Balance:", balance)

    print("\n===== EXPENSES BY CATEGORY =====")

    if len(categories) == 0:
        print("No expenses recorded.")

    else:
        for category, amount in categories.items():
            print(category, ":", amount)


# Main program
data = load_data()

while True:

    print("\n==============================")
    print("       EXPENSE TRACKER")
    print("==============================")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_income(data)

    elif choice == "2":
        add_expense(data)

    elif choice == "3":
        view_transactions(data)

    elif choice == "4":
        view_summary(data)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")