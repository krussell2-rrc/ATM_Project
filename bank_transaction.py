"""
Description: 
Author: Kareem Russell
Date: September 30, 2023
Usage:
"""

D = ["Deposit"]
W = ["Withdraw"]
Q = ["Quit"]

import random
users_bank_balance = random.randint(-1000, 10000)
users_bank_balance = "4298"
float(users_bank_balance)
print(float(users_bank_balance))

border = "****************************************"
print(border)

pixell = "PIXELL RIVER FINANCIAL"
pixell_centered = pixell.center(40)
print(pixell_centered)

atm_simulator = "ATM Simulator"
atm_simulator_centered = atm_simulator.center(40)
print(atm_simulator_centered)

current_balance = (float(users_bank_balance))
current_balance_message = (f"Your current balance is: ${current_balance}")
current_balance_message_centered = current_balance_message.center(40)
print(current_balance_message_centered)

deposit_input = ("Deposit: D")
deposit_input_centered = deposit_input.center(40)
print(deposit_input_centered)

withdraw_input = ("Withdraw: W")
withdraw_input_centered = withdraw_input.center(40)
print(withdraw_input_centered)

quit_input = ("To Quit: Q")
quit_input_centered = quit_input.center(40)
print(quit_input_centered)

print(border)