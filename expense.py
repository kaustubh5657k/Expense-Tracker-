#Expenses Tracker 
expensesList = [] #List of expenses in form of dictionary
print("Welcome to Expensese tracker")

while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View All Expenses ")
    print("3. View Total Amount")
    print("4. Exit")

    choice = int(input('pleases Enter Your Choice :'))

    #ADD EXPENSES
    if(choice==1):
        date = input("On Which date did you spend the money? : ")
        category = input("Which type of spend it?(Food, Travel, Book, etc..)")
        description = input("Give me More details :")
        amount = float(input("Enter the amount : "))

        expense ={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }

        expensesList.append(expense)
        print("\n Done . Expense is added succesfully")

        #2. View All Expenses
    elif(choice == 2):
        if(len(expensesList)==0):
            print("No Expenses Added Go the spend it..")
        else:
            print('====This is yours All expenses===')
            count = 1
            for eachExpenses in expensesList:
                print(f"Kharcha Number {count} -> {eachExpenses["date"]}, {eachExpenses["category"]}, {eachExpenses["description"]}, {eachExpenses["amount"]} ")
                count= count +1

                #3. View Total Spending
    elif(choice==3):

        total = 0
        for eachExpenses in expensesList:
            total = total + eachExpenses["amount"]
        print("\n TOTAL EXPENSES = ",total)

        #4. Exit
    elif(choice == 4):
        print("Thanks For Visiting....")
        break

    else:
        print("INVALID CHOICE . TRY AGAIN")
