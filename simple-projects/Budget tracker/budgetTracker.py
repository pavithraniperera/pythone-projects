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

def main():
    print("Welcome to the Budget App")
    initial_budget = float(input("Enter your initial budget: "))
    budget = initial_budget
    expences = []

    while True:
        print("What would you like to do?\n")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expences, description, amount)
        elif choice == "2":
            show_budget_details(budget, expences)
        elif choice == "3":
            print("Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
