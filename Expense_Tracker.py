from datetime import datetime

class Expense:
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"{self.date} | {self.category} | ₹{self.amount} | {self.description}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        exp = Expense(amount, category, description)
        self.expenses.append(exp)
        print("\n✅ Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return
        print("\n----- All Expenses -----")
        for idx, exp in enumerate(self.expenses, start=1):
            print(f"{idx}. {exp}")

    def total_expense(self):
        total = sum(e.amount for e in self.expenses)
        print(f"\n💰 Total Spending: ₹{total}")

    def category_summary(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return

        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount

        print("\n📊 Category-wise Summary:")
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
                print("Invalid amount. Please enter a number.")
                continue

            category = input("Enter Category (e.g., Food, Travel, Bills): ")
            description = input("Enter Description (optional): ")
            tracker.add_expense(amount, category, description)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expense()

        elif choice == "4":
            tracker.category_summary()

        elif choice == "5":
            print("\nThank you for using Expense Tracker! 👋")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
