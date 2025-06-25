import csv
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense(amount, category):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount])
    print("✅ Expense added.")

def view_expenses():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            total = 0
            print("\n📜 Your Expenses:")
            print("-" * 30)
            for row in reader:
                print(f"{row[0]} | {row[1]:<10} | ₹{row[2]}")
                total += float(row[2])
            print("-" * 30)
            print(f"💰 Total Spent: ₹{total}")
    except FileNotFoundError:
        print("📂 No expense data found.")

def main():
    print("📊 Expense Tracker")
    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("👉 Enter your choice (1-3): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount (₹): "))
                category = input("Enter category (e.g. Food, Travel): ")
                add_expense(amount, category)
            except ValueError:
                print("❌ Invalid amount.")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
