# Initialize account balance
balance = 1000.0
while True:
    print('''\nATM Menu:)
                1. Check Balance
                2. Deposit Money
                3. Withdraw Money
                4. Exit''')

    # Get user choice1
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print(f"\nYour balance is: ${balance:.2f}")

    elif choice == 2:
        deposit = float(input("\nEnter the amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print(f"\nYou have deposit ${deposit:.2f}")
            print(f"Your new balance is: ${balance:.2f}")
        else:
            print("\nInvalid deposit amount")
    elif choice == 3:
        withdraw = float(input("\nEnter the amount to withdraw: "))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print(f"\nYou have withdraw ${withdraw:.2f}")
            print(f"Your new balance is: ${balance:.2f}")
        else:
            print("Insufficient funds!")
    elif choice == 4:
        print("Thank you for using the ATM!")
        break
    else:
        print("\nInvalid input, please try again.")