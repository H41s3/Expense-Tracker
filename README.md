# Expense Tracker

An intuitive and simple Python-based Expense Tracker to manage your expenses effectively. This application uses SQLite for data storage and includes features such as categorization, date filtering, visualizations, and exporting data to CSV.

## Features

1. **Add Expenses**: Record expenses with a description, amount, and category.
2. **View All Expenses**: Display all recorded expenses.
3. **Filter by Category**: View expenses based on their category.
4. **Filter by Date**: Retrieve expenses within a specific date range.
5. **Monthly Report**: Generate a summary report of expenses for a specific month.
6. **Visualize Expenses**: Plot expenses by category using a bar chart.
7. **Export to CSV**: Save all expense data into a CSV file.
8. **Delete Expense**: Remove an expense by its unique ID.

## Requirements

- Python 3.8 or higher
- Required libraries: `sqlite3`, `datetime`, `matplotlib`, `csv`

Install missing libraries using pip:
```bash
pip install matplotlib
```

## How to Run

1. Clone this repository or copy the script to your local machine.
2. Run the script:
   ```bash
   python expense_tracker.py
   ```
3. Use the menu options to manage your expenses.

## Menu Options

1. **Add an expense**: Add a new expense by providing details.
2. **View all expenses**: List all expenses stored in the database.
3. **View expenses by category**: Filter and view expenses by category.
4. **View expenses by date**: Specify a date or date range to view expenses.
5. **Generate monthly report**: Enter a month (e.g., `2025-01`) to get a category-wise breakdown of expenses.
6. **Plot expenses by category**: Generate a bar chart for expenses by category.
7. **Export expenses to CSV**: Save all expenses into a CSV file for offline viewing.
8. **Delete an expense**: Delete a specific expense by its ID.
9. **Exit**: Close the application.

## Example

### Adding an Expense:
```
Enter description: Coffee
Enter amount: 5.50
Enter category: Food
Expense added successfully.
```

### Generating a Monthly Report:
```
Enter month (YYYY-MM): 2025-01

Monthly Report for 2025-01:
Category: Food, Total: $50.00
Category: Transportation, Total: $30.00
```

### Visualizing Expenses:
A bar chart displaying the total amount spent per category.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
