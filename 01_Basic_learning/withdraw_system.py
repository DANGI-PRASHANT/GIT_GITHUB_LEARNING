
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

