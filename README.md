# 💰 Personal Finance Tracker

A simple command-line personal finance tracker built with Python. Track your income and expenses, categorize transactions, and get financial summaries.

## Features

- ✅ **Add Transactions** - Record income and expenses with descriptions and categories
- 📋 **View Transactions** - Display all transactions in a formatted table
- 💰 **Balance Calculation** - See your current financial balance
- 📊 **Financial Summary** - Get total income, expenses, and net balance
- 🏷️ **Category Breakdown** - Analyze spending by category
- 🗑️ **Delete Transactions** - Remove incorrect entries
- 💾 **Data Persistence** - Automatically saves data to JSON file
- 🇪🇺 **Euro Currency** - All amounts displayed in euros (€)

## Installation

1. **Clone or download** this repository
2. **Navigate** to the project directory:
   ```bash
   cd finance-tracker
   ```
3. **Run** the application:
   ```bash
   python src/finance_tracker.py
   ```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Usage

### Adding a Transaction
1. Choose option `1` from the main menu
2. Enter the amount in euros
3. Add a description
4. Choose to use today's date or enter a custom date
5. Specify a category (e.g., "Food", "Salary", "Utilities")
6. Select transaction type: `income` or `expense`

### Viewing Your Data
- **Option 2**: View all transactions in a table format
- **Option 3**: See your current balance
- **Option 4**: Get a complete financial summary
- **Option 5**: View spending breakdown by category

### Managing Transactions
- **Option 6**: Delete a transaction by selecting its number
- **Option 7**: Manually save your data (auto-saves after each transaction)

## Data Storage

Your transaction data is automatically saved to `transactions.json` in the same directory as the script. This file is created automatically and loads your previous transactions when you restart the program.

## Example Usage

```
=== 💰 Personal Finance Tracker ===
1. Add Transaction
2. View All Transactions
3. View Balance
4. View Summary
5. View Category Breakdown
6. Delete Transaction
7. Save Data
8. Exit

Enter your choice (1-8): 1
Enter amount: €50.00
Enter description: Grocery shopping
Use today's date? (y/n): y
Enter category: Food
Enter type (income/expense): expense
✅ Transaction added successfully!
```

## File Structure

```
finance-tracker/
├── src/
│   └── finance_tracker.py    # Main application
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── transactions.json        # Data file (created automatically)
```


## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.
