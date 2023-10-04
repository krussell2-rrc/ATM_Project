"""
Description: 
Author: Kareem Russell
Date: September 30, 2023
Usage:
"""

interface_values = ["W", "D", "Q"]

import random
users_bank_balance = random.randint(-1000, 10000)
users_bank_balance = "4298"
users_bank_balance = float(users_bank_balance)
print(float(users_bank_balance))

border = "****************************************"
print(border)

pixell = "PIXELL RIVER FINANCIAL"
print(pixell.center(40))

atm_simulator = "ATM Simulator"
print(atm_simulator.center(40))

current_balance = (float(users_bank_balance))
current_balance_message = (f"Your current balance is: ${current_balance}")
print(current_balance_message.center(40))

deposit_input = ("Deposit: D")
print(deposit_input.center(40))

withdraw_input = ("Withdraw: W")
print(withdraw_input.center(40))

quit_input = ("To Quit: Q")
print(quit_input.center(40))
print(border)

invalid_selection = "INVALID SELECTION"
insufficient_funds = "INSUFFICIENT FUNDS"

selection = input("Enter your selection: ")
if selection not in interface_values:
    print(border)
    print(invalid_selection.center(40))
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
        print(insufficient_funds.center(40))
        print(border)
    else:
        users_bank_balance - transaction_amount
        print(border)
        print(f"Your current balance is {users_bank_balance - transaction_amount: 2f}")
        print(border)



    




    

    









    

    



