card = True
balance = 500

pin = 1234

if pin == 1234:

    option = input("(Balance check) / (Withdraw) / (Deposit) : " )

    if option == "Balance check":
        print(f"Your Balance is {balance} $.")

       
    elif option == "withdraw":

            withdraw = int(input("Enter amount: "))

            if withdraw >= balance:
                print("Insufficent Balance")
            else:
                print("Withdraw Successful")
                print(f"Remaining amount is {balance - withdraw} $")


            # Deposit features:

    elif option.lower() == "deposit":

            deposit = int(input("Enter a amount: "))
            print()

            balance_01 = balance + deposit

            if balance_01 == balance + deposit:
                print(f"Deposit amount is {deposit} $")
                print(f"Total Balance is {balance_01} $")

