import json

def add_expense(expences, description, amount):
    expences.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")

def get_Total_expences(expences):
    total = 0
    for expence in expences:
        total += expence["amount"]
    return total

def get_balance(budget, expences):
    return budget - get_Total_expences(expences)

def show_budget_details(budget, expences):
    print(f"Total budget: {budget}")
    print("Expenses:")
    for expence in expences:
        print(f" .{expence['description']}: {expence['amount']}")
    print(f"Total spent: {get_Total_expences(expences)}")
    print(f"Remaining budget: {get_balance(budget, expences)}")
    
def load_budget_data(filePath):
    try:
        with open(filePath, "r") as file:
            data = json.load(file)
            return data["initial_budget"], data["expences"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def save_budget_data(filePath, initial_budget, expences):
    data = {
       "initial_budget": initial_budget,
       "expences": expences  
    }
    with open(filePath, "w") as file:
        json.dump(data, file, indent=4)

def main():
    print("Welcome to the Budget App")
    filePath = 'budget_data.json'
    
    # Load data from the file if available
    initial_budget, expences = load_budget_data(filePath)
    
    if initial_budget == 0:  # No budget saved, ask user for input
        initial_budget = float(input("Enter your initial budget: "))

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expences, description, amount)
        elif choice == "2":
            show_budget_details(initial_budget, expences)
        elif choice == "3":
            save_budget_data(filePath, initial_budget, expences)
            print("Data saved. Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()



# Project: Budget Tracker App
# This Budget Tracker App helps users manage their personal finances by tracking expenses and displaying budget details. Users can:

# Add expenses with a description and amount.
# View their total budget, total expenses, and remaining balance.
# Save the budget and expense data to a file (budget_data.json), so the data persists between sessions.
# The app reads from and writes to a JSON file to store budget data, allowing users to resume their financial tracking at any time.