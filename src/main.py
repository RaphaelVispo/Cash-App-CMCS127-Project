"""
This file will be the main flow of the program
"""
from expense import *
from group import *
from user import *
from friends import *

user = "3xyaufSzzUp9LPkSKTxhqz"

get_unpaid_expenses(user)
get_paid_expenses(user)
get_total_paid_expenses(user)
get_total_unpaid_expenses(user)
get_total_expenses(user)
get_friends(user)
get_username(user)
get_groups(user)


def choose_Efg():
    global efg_Choice
    while True:
        try:
            print("[1] EXPENSE")
            print("[2] FRIEND")
            print("[3] GROUP")

            efg_Choice = int(input("Your choice: "))
            if efg_Choice > 0 and efg_Choice < 4:
                return efg_Choice
                break;
            else:
                print("Invalid entry. Please try again.")
        except:
            print("Invalid entry. Please try again.\n")
            continue
            
def choose_View():
    global view_Choice
    while True:
        try:
            print("What would you like to view?")
            print("[1] ALL EXPENSES MADE WITH WITHIN A MONTH")
            print("[2] ALL EXPENSES MADE WITH A FRIEND")
            print("[3] ALL EXPENSES MADE WITH A GROUP")
            print("[4] CURRENT BALANCE FROM ALL EXPENSES")
            print("[5] ALL FRIENDS WITH OUTSTANDING BALANCE")
            print("[6] ALL GROUPS")
            print("[7] ALL GROUPS WITH OUTSTANDING BALANCE")
            print("What would you like to view?")

            view_Choice = int(input("Your choice: "))
            if view_Choice > 0 and view_Choice < 7:
                return view_Choice
                break;
            else:
                print("Invalid entry. Please try again.")
        except:
            print("Invalid entry. Please try again.\n")
            continue



while True:
    try:
        print("Welcome to Cash-App kineme\n")
        print("[1] ADD")
        print("[2] DELETE")
        print("[3] SEARCH")
        print("[4] UPDATE")
        print("[5] VIEW")
        print("[0] EXIT CASH-APP")
    
        action = int(input("\nWhat would you like to do? "))
        if action >= 0 and action <= 5:
            break;
        else:
            print("Invalid entry. Please try again.\n")
    except ValueError:
        print("Invalid entry. Please try again.\n")
        continue
## instead of print, lagay yung function for it
if action == 1:
    print("What would you like to add?")
    choose_Efg()
    if efg_Choice == 1:
        print("Add expense")
    elif efg_Choice == 2:
        print("Add friend")
    elif efg_Choice == 3:
        print("Add group")
    

elif action == 2:
    print("What would you like to delete?")
    choose_Efg()
    if efg_Choice == 1:
        print("delete expense")
    elif efg_Choice == 2:
        print("delete friend")
    elif efg_Choice == 3:
        print("delete group")

elif action == 3:
    print("What would you like to search?")
    choose_Efg()
    if efg_Choice == 1:
        print("search expense")
    elif efg_Choice == 2:
        print("search friend")
    elif efg_Choice == 3:
        print("search group")

elif action == 4:
    print("What would you like to update?")
    choose_Efg()
    if efg_Choice == 1:
        print("update expense")
    elif efg_Choice == 2:
        print("update friend")
    elif efg_Choice == 3:
        print("update group")

elif action == 5:
    choose_View()
    if view_Choice == 1:
        print("expense month")
    elif view_Choice == 2:
        print("expense friend")
    elif view_Choice == 3:
        print("expense group")
    elif view_Choice == 4:
        print("expense balance")
    elif view_Choice == 5:
        print("friend balance")
    elif view_Choice == 6:
        print("all groups")
    elif view_Choice == 7:
        print("group balance")

elif action == 0:
    print("You have exited CASH-APP")

if action != 0:    
    print("Thank you for using CASH-APP!!")
