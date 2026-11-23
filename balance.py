print("===== BANK BALANCE CHECK =====")

account_number = input("Enter your Account Number: ")
pin = input("Enter your PIN: ")

correct_account = "1234567809"
correct_pin = "1999"
balance = 25000

if account_number == correct_account and pin == correct_pin:
    print("\nLogin Successful!")
    print("Your Bank Balance is: ₹", balance)

else:
    print("\nInvalid Account Number or PIN!")
