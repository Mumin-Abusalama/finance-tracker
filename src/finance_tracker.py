import json
import os
from datetime import datetime


class Transactions:
    def __init__(self, filename="transactions.json"):
        self.transactions = []
        self.filename = filename
        self.load_transactions()

    def save_transactions(self):
        """Save transactions to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.transactions, file, indent=4)
        except Exception as e:
            print(f"Error saving transactions: {e}")

    def load_transactions(self):
        """Load transactions from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.transactions = json.load(file)
                print(f"Loaded {len(self.transactions)} transactions.")
            except Exception as e:
                print(f"Error loading transactions: {e}")
                self.transactions = []
        else:
            self.transactions = []

    def add_transaction(self, amount, description, date, category, transaction_type):
        transaction = {
            "Amount": amount,
            "Description": description,
            "Date": date,
            "Category": category,
            "Type": transaction_type
        }
        self.transactions.append(transaction)
        self.save_transactions()

    def display_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return
        
        print(f"\n{'Type':<10} {'Amount':<12} {'Date':<12} {'Category':<15} {'Description':<20}")
        print("-" * 75)
        for transaction in self.transactions:
            print(f"{transaction['Type']:<10} €{transaction['Amount']:<10.2f} {transaction['Date']:<12} {transaction['Category']:<15} {transaction['Description']:<20}")

    def get_balance(self):
        """Calculate current balance"""
        balance = 0
        for transaction in self.transactions:
            if transaction['Type'] == 'income':
                balance += transaction['Amount']
            else:
                balance -= transaction['Amount']
        return balance

    def get_summary(self):
        """Get income and expense summary"""
        total_income = sum(t['Amount'] for t in self.transactions if t['Type'] == 'income')
        total_expenses = sum(t['Amount'] for t in self.transactions if t['Type'] == 'expense')
        return total_income, total_expenses

    def get_category_summary(self):
        """Get spending by category"""
        categories = {}
        for transaction in self.transactions:
            category = transaction['Category']
            amount = transaction['Amount']
            if category not in categories:
                categories[category] = {'income': 0, 'expense': 0}
            categories[category][transaction['Type']] += amount
        return categories

    def delete_transaction(self, index):
        """Delete transaction by index"""
        if 0 <= index < len(self.transactions):
            removed = self.transactions.pop(index)
            self.save_transactions()
            return removed
        return None


def main():
    tracker = Transactions()

    while True:
        print("\n=== 💰 Personal Finance Tracker ===")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. View Balance")
        print("4. View Summary")
        print("5. View Category Breakdown")
        print("6. Delete Transaction")
        print("7. Save Data")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            # Validate amount
            while True:
                try:
                    amount = float(input("Enter amount: €"))
                    if amount <= 0:
                        print("Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number for amount.")
    
            description = input("Enter description: ")
            
            # Auto-fill today's date or let user enter custom date
            use_today = input("Use today's date? (y/n): ").lower()
            if use_today == 'y':
                date = datetime.now().strftime("%Y-%m-%d")
            else:
                date = input("Enter date (YYYY-MM-DD): ")
            
            category = input("Enter category: ")
    
            # Validate transaction type
            while True:
                transaction_type = input("Enter type (income/expense): ").lower()
                if transaction_type in ["income", "expense"]:
                    break
                else:
                    print("Please enter 'income' or 'expense'.")
    
            tracker.add_transaction(amount, description, date, category, transaction_type)
            print("✅ Transaction added successfully!")

        elif choice == 2:
            print("\n--- All Transactions ---")
            tracker.display_transactions()
        
        elif choice == 3:
            balance = tracker.get_balance()
            print(f"\n💰 Current Balance: €{balance:.2f}")
            
        elif choice == 4:
            income, expenses = tracker.get_summary()
            balance = income - expenses
            print(f"\n--- Financial Summary ---")
            print(f"📈 Total Income:  €{income:.2f}")
            print(f"📉 Total Expenses: €{expenses:.2f}")
            print(f"💰 Net Balance:   €{balance:.2f}")
            
        elif choice == 5:
            categories = tracker.get_category_summary()
            print(f"\n--- Category Breakdown ---")
            for category, amounts in categories.items():
                net = amounts['income'] - amounts['expense']
                print(f"{category}: Income €{amounts['income']:.2f}, Expenses €{amounts['expense']:.2f}, Net: €{net:.2f}")
                
        elif choice == 6:
            print("\n--- Delete Transaction ---")
            tracker.display_transactions()
            if tracker.transactions:
                try:
                    index = int(input("Enter transaction number to delete (1-based): ")) - 1
                    if 0 <= index < len(tracker.transactions):
                        removed = tracker.delete_transaction(index)
                        print(f"✅ Deleted: {removed['Description']}")
                    else:
                        print("Invalid transaction number.")
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == 7:
            tracker.save_transactions()
            print("💾 Data saved successfully!")
            
        elif choice == 8:
            print("👋 Thanks for using Finance Tracker!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()