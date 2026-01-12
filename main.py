from datetime import datetime
import json
import csv
import os
def show_menu():
    print("\n1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Filter by Category")
    print("5. Filter by Date")
    print("6. Exit")

expenses=[]

def load_expenses():
    global expenses
    try:
        with open('expenses.json', 'r') as file:
            expenses=json.load(file)
            print(f"Loaded {len(expenses)} expenses") # Debug line
    except FileNotFoundError:
        expenses=[]
        print("No previous expenses found")  # Debug line
load_expenses()


def save_expenses():
    print("Saving to:", os.path.abspath("expenses.json"))
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
    print(f"✓ Saved {len(expenses)} expenses")


def Add_Expenses():
    amount=float(input("Enter amount: "))
    category=input("Enter category: ")
    description=input("Enter description: ")

    date=datetime.now().strftime("%Y-%m-%d")

    expenses.append({
        'amount':amount,
        'category':category,
        'description':description,
        'date':date
        })
    
    print(f"DEBUG: expenses list now has {len(expenses)} items")
    print(f"DEBUG: Last expense added: {expenses[-1]}")

    save_expenses()

    print("Expense Added!\n")
    


def View_Expenses():
    if not expenses:
        print("No Expenses Yet!\n")
        return
    
    for i,e in enumerate(expenses, start=1):
        print(f"{i}.{e.get('date', 'no date')} | ₹{e['amount']} | {e['category']} | {e['description']}")

    print()


def export_to_csv(expenses_to_export,filename):
    if not expenses_to_export:
        print("No data to export. ")
        return
    with open(filename, 'w', newline='') as file:
        writer=csv.writer(file)
        #header row
        writer.writerow(['Date','Amount','Category','Description'])
        for e in expenses_to_export:
            writer.writerow([
                e.get('date', 'No Date'),
                e['amount'],
                e['category'],
                e['description']
            ])
    print(f"Exported to {filename}\n")


def Total_Expenses():
    print("HELLO FROM TOTAL EXPENSES FUNCTION!")  # Test if function is called
    total = sum(e['amount'] for e in expenses)
    print(f"\nTotal Expenses: ₹{total}\n")


def Filter_by_Category():
    if not expenses:
        print("\nNo Expenses Yet.\n")
        return
    category=input("Enter category to filter: ").lower()
    found=False
    print()
    for i,e in enumerate(expenses, start=1):
        if e['category'].lower()==category:
            print(f"{i}.{e.get('date', 'no date')} | ₹{e['amount']} | {e['category']} | {e['description']}")
            found=True
    if not found:
        print("No expenses found in this category.")
    print()


def filter_by_date():
    if not expenses:
        print("\nNo expenses yet to filter.\n")
        return
    start_date=input("Enter start date (YYYY-MM-DD): ")
    end_date=input("Enter end date (YYYY-MM-DD): ")

    filtered=[]
    print()
    
    for e in expenses:
        expense_date=e.get('date')
        if expense_date and start_date <= expense_date <= end_date:
            filtered.append(e)
    
    if not filtered:
        print("No expenses found in this date range. \n")
        return
    
    for i,e in enumerate(filtered, start=1):
        print(f"{i}.{e.get('date')} | ₹{e['amount']} | {e['category']} | {e['description']}")
    
    print()

    export=input("Do you want to export these results to CSV? (y/n): ").lower()
    if export=='y':
        export_to_csv(filtered,"filtered_expenses.csv")


def main():

    while True:

        show_menu()

        choice=input("Choose an option:")
        if choice=='1':
            Add_Expenses()
        elif choice=='2':
            View_Expenses()
        elif choice=='3':
            Total_Expenses()
        elif choice=='4':
            Filter_by_Category()
        elif choice=='5':
            filter_by_date()
        elif choice=='6':
            print("Exiting...")
            break
        else:
            print("Invalid Choice. Try Again.")

main()



