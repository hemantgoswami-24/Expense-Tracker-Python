from datetime import datetime
import csv
import os

FILE_NAME = "expenses.csv"


class Expense:
    def __init__(self, amount, category, description="", date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"{self.date} | {self.category} | ₹{self.amount} | {self.description}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    # 🔹 Load data from file
    def load_expenses(self):
        if not os.path.exists(FILE_NAME):
            return

        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    date, amount, category, description = row
                    self.expenses.append(
                        Expense(float(amount), category, description, date)
                    )

    # 🔹 Save single expense to file
    def save_expense(self, expense):
        with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [expense.date, expense.amount, expense.category, expense.description]
            )

    def add_expense(self, amount, category, description=""):
        exp = Expense(amount, category, description)
        self.expenses.append(exp)
        self.save_expense(exp)
        print("\n Expense added & saved successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return

        print("\n----- All Expenses -----")
        for idx, exp in enumerate(self.expenses, start=1):
            print(f"{idx}. {exp}")

    def total_expense(self):
        total = sum(e.amount for e in self.expenses)
        print(f"\n Total Spending: ₹{total}")

    def category_summary(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return

        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount

        print("\n Category-wise Summary:")
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")


def main_menu():
    tracker = ExpenseTracker()

    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Spending")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter Amount: ₹"))
            except ValueError:
                print("Invalid amount")
                continue

            category = input("Enter Category (Food, Travel, Bills): ")
            description = input("Enter Description (optional): ")
            tracker.add_expense(amount, category, description)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expense()

        elif choice == "4":
            tracker.category_summary()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
