import csv
from datetime import datetime

STARTING_BALANCE = 50000.0
FILE_NAME = 'expenses.csv'

def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Item', 'Amount'])
    except FileExistsError:
        pass

def add_expense(item, amount):
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), item, amount])
    print(f"✔️ Added '{item}' - Ksh {amount}")

def show_summary():
    total_spent = 0
    expenses = []

    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                amount = float(row['Amount'])
                total_spent += amount
                expenses.append(row)
    except FileNotFoundError:
        print("No expense data found.")
        return

    remaining = STARTING_BALANCE - total_spent

    print("\n📋 Saved Expenses:")
    print("{:<12} {:<20} {:>10}".format("Date", "Item", "Amount (Ksh)"))
    print("-" * 45)
    for exp in expenses:
        print("{:<12} {:<20} {:>10.2f}".format(exp['Date'], exp['Item'], float(exp['Amount'])))

    # ✅ Move these inside the function
    print("\n📊 Expense Summary:")
    print(f"  Total Spent      : Ksh {total_spent:.2f}")
    print(f"  Remaining Balance: Ksh {remaining:.2f}")

# Example usage
initialize_file()
add_expense("Groceries", 2500)
add_expense("Transport", 1200)
show_summary()
 
 