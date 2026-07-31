from datetime import datetime 
import json

def menu():
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Total Expenses")
    print("5. Delete Expense")
    print("6. Monthly Summary")
    print("7. Exit")
    global choice 
    
    try:
        choice = int(input("Enter choice (1/2/3/4/5/6/7) : "))
    except ValueError:
        print("Please enter a valid choice.")

# list of dictionaries
expenses = []
def add_expense():
    category = str(input("Enter Category of expense :"))
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    description = input("Enter Description about expense :")
    date = datetime.now().strftime("%d-%m-%Y %H:%M")

    expenses.append({
        'Category' : category,
        'Amount' : amount,
        'Description' : description,
        'Date' : date
    })
    save_data()

def save_data():
    with open("expenses.json",'w')as file:
        json.dump(expenses,file,indent=5)
    print("Data saved successfully.")

def load_data():
    global expenses

    try:
        with open('expenses.json','r')as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def view_expenses():
    if not expenses:
        print("No expenses found.")
    
    print("="*100)
    print(f"{'Date':<20}{'Category':<15}{'Description':<25}{'Amount':<15}")
    print("-"*95)

    for ex in expenses:
        print(f"{ex['Date']:<20}{ex['Category']:<15}{ex['Description']:<25}{ex['Amount']:<15}")
    print("="*100)

def search_by_category():
    searchid = input("Enter Category you have to filter :")
    print("Category = ",searchid)
    print("="*100)
    print(f"{'Date':<20}{'Description':<65}{'Amount':<15}")
    print("-"*100)
    for ex in expenses:
        if ex['Category'].lower() == searchid.lower():
            print(f"{ex['Date']:<15}{ex['Description']:<65}{ex['Amount']:<15}")
            print("="*100)

def total_expenses():
    total = 0
    for ex in expenses:
        total += ex['Amount']
    print("Total Expenses = Rs.",total)

def summary():
    if not expenses:
        print("No expenses found.")
        return

    month = input("Enter Month (MM): ")

    summary = {}

    for ex in expenses:
        parts = ex["Date"].split("-")
        if parts[1] == month:
            category = ex["Category"]
            if category in summary:
                summary[category] += ex["Amount"]
            else:
                summary[category] = ex["Amount"]
                
    if not summary:
        print("No expenses found for this month.")
        return
    print("\n===== Monthly Summary =====")
    total = 0
    for category, amount in summary.items():
        print(f"{category:<15} Rs. {amount}")
        total += amount
    print("---------------------------")
    print(f"Total = Rs. {total}")
            
        

def delete_expense():
    b = input("Enter Category :")
    d = input("Enter Date :")
    for ex in expenses:
        if ex['Category']==b and ex['Date']==d:
            q = input("Do you want to delete student info (y/n) :")
            if q=='y':
                expenses.remove(ex)
                print("deleted successfully")
            else:
                print("Deletion cancelled")
    save_data()

print("====================================================")
print("                 Expense Tracker                    ")
print("====================================================")
load_data()
while True:
    print("\n Choose menu below to do operations : \n")
    
    menu()
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        search_by_category()
    elif choice == 4:
        total_expenses()
    elif choice == 5:
        delete_expense()
    elif choice == 6:
        summary()
    elif choice==7:
        print("Exiting menu...")
        break
    else:
        print("Invalid Choice, Try again...")
