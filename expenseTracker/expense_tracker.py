import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import csv

# Connect to SQLite database
def create_db():
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()

    # Create expenses table with category
    cur.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL,
        category TEXT
    )
    ''')

    conn.commit()
    conn.close()

create_db()

# Function to add a new expense
def add_expense(description, amount, category):
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    
    date = datetime.now().strftime('%Y-%m-%d')
    
    cur.execute('INSERT INTO expenses (description, amount, date, category) VALUES (?, ?, ?, ?)', 
                (description, amount, date, category))
    
    conn.commit()
    conn.close()
    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM expenses')
    expenses = cur.fetchall()
    
    for expense in expenses:
        print(f"ID: {expense[0]}, Description: {expense[1]}, Amount: ${expense[2]}, Date: {expense[3]}, Category: {expense[4]}")
    
    conn.close()

# View expenses by category
def view_expenses_by_category(category):
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM expenses WHERE category = ?', (category,))
    expenses = cur.fetchall()
    
    for expense in expenses:
        print(f"ID: {expense[0]}, Description: {expense[1]}, Amount: ${expense[2]}, Date: {expense[3]}, Category: {expense[4]}")
    
    conn.close()

# View expenses by date range
def view_expenses_by_date(start_date, end_date=None):
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    
    if end_date:
        cur.execute('SELECT * FROM expenses WHERE date BETWEEN ? AND ?', (start_date, end_date))
    else:
        cur.execute('SELECT * FROM expenses WHERE date = ?', (start_date,))
    
    expenses = cur.fetchall()
    
    for expense in expenses:
        print(f"ID: {expense[0]}, Description: {expense[1]}, Amount: ${expense[2]}, Date: {expense[3]}, Category: {expense[4]}")
    
    conn.close()

# Generate a report for a specific month
def generate_monthly_report(month):
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    
    cur.execute('SELECT category, SUM(amount) FROM expenses WHERE date LIKE ? GROUP BY category', 
                (f'{month}%',))
    
    report = cur.fetchall()
    
    print(f"\nMonthly Report for {month}:")
    for category, total in report:
        print(f"Category: {category}, Total: ${total}")
    
    conn.close()

# Plot expenses by category using a bar chart
def plot_expenses_by_category():
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    
    cur.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    data = cur.fetchall()
    
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]
    
    plt.bar(categories, amounts)
    plt.xlabel('Category')
    plt.ylabel('Total Spent')
    plt.title('Spending by Category')
    plt.show()

    conn.close()

# Export expenses to a CSV file
def export_expenses_to_csv(filename='expenses.csv'):
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM expenses')
    expenses = cur.fetchall()
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Description', 'Amount', 'Date', 'Category'])
        writer.writerows(expenses)
    
    conn.close()
    print(f"Expenses exported to {filename}")

# Function to delete an expense by ID
def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cur = conn.cursor()
    
    # Delete the expense based on the provided ID
    cur.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    
    if cur.rowcount == 0:
        print(f"No expense found with ID {expense_id}.")
    else:
        print(f"Expense with ID {expense_id} deleted successfully.")
    
    conn.commit()
    conn.close()

# Main Application Loop
def main():
    create_db()  # Ensure the database is created

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View expenses by category")
        print("4. View expenses by date")
        print("5. Generate monthly report")
        print("6. Plot expenses by category")
        print("7. Export expenses to CSV")
        print("8. Delete an expense")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(description, amount, category)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category = input("Enter category: ")
            view_expenses_by_category(category)
        elif choice == '4':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (optional, YYYY-MM-DD): ")
            view_expenses_by_date(start_date, end_date)
        elif choice == '5':
            month = input("Enter month (YYYY-MM): ")
            generate_monthly_report(month)
        elif choice == '6':
            plot_expenses_by_category()
        elif choice == '7':
            filename = input("Enter filename for export (e.g., expenses.csv): ")
            export_expenses_to_csv(filename)
        elif choice == '8':
            expense_id = int(input("Enter the ID of the expense to delete: "))
            delete_expense(expense_id)
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
