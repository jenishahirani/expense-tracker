#Expense Tracker project

expenseList= [] # List of expences in form of dictionary
print("Welcome to expense Tracker!")

while True:
    print("-------Menu-------")
    print("1.Add Expense")
    print("2.View All expenses")
    print("3.View Total kharcha")
    print("4.Exit!!")

    choice=int(input("Please Enter your choice:"))
    # add expense
    if(choice==1):
        date= input("Kis date par kharcha kiya tha?")
        categary= input("kis type ka kharcha kiya tha?(Food,Travel,Makeup,Books)")
        description= input("Aur details dedo")
        amount= float(input("Enter the amount:"))

        expense={
            "date":date,
            "categary":categary,
            "description":description,
            "amount":amount,
        }
        expenseList.append(expense)
        print("\nDone bro! Expense is Added successfully.")

    #view all expense
    elif(choice==2):   
        if(len(expenseList)==0):
            print("No expenses Added. Jao pehle kharcha karo.")
        else:
            print("==== Ye he apka sara expense ====")
            count =1
            for eachkharcha in expenseList:
                print(f"Kharcha number{count}:{eachkharcha["date"]},{eachkharcha["categary"]},{eachkharcha["description"]},{eachkharcha["amount"]}")
                count = count +1

    #view Total spending 
    elif(choice==3):
        total= 0
        for eachkharcha in expenseList:
            total= total+eachkharcha["amount"]

        print("Total kharcha:",total)
    #exit
    elif(choice== 4):
        print("Dhanyawad apne hamara system use kiya!")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")


            

 

