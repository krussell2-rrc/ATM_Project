"""
Description: 
Author: Kareem Russell
Date: September 30, 2023
Usage:
"""

interface_values = ["W", "D", "Q"]

import random
users_bank_balance = random.randint(-1000, 10000)
users_bank_balance = float(users_bank_balance)
print(float(users_bank_balance))

border = "****************************************"
print(border)
print("PIXELL RIVER FINANCIAL".center(40))
print("ATM Simulator".center(40))
current_balance = (float(users_bank_balance))
current_balance_message = (f"Your current balance is: ${current_balance}")
print(current_balance_message.center(40))
print("Deposit: D".center(40))
print("Withdraw: W".center(40))
print("To Quit: Q".center(40))
print(border)

selection = input("Enter your selection: ")
if selection not in interface_values:
    print(border)
    print("INVALID SELECTION".center(40))
    print(border)
else: transaction_amount = float(input("Enter amount of transaction: "))
if transaction_amount < 0:
    print("Invalid transaction amount")
elif selection == "D":
    users_bank_balance + transaction_amount
    print(border)
    print(f"Your new balance is: {users_bank_balance + transaction_amount: 2f}")
    print(border)
elif selection == "W":
    if transaction_amount > users_bank_balance:
        print(border)
        print("INSUFFICIENT_FUNDS".center(40))
        print(border)
    else:
        users_bank_balance - transaction_amount
        print(border)
        print(f"Your current balance is {users_bank_balance - transaction_amount: 2f}")
        print(border)






    




    

    









    

    



