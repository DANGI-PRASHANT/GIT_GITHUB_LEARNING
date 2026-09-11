num1 = float(input("Enter a Number_01: "))
num2 = float(input("Entera Number_02: "))

print()
print(f"Sum of two number : {num1 + num2}")
print(f"Sub of two number : {num1 -num2}")
print(f"Multiple of two number: {num1 * num2}")
print(f"Divided : {num1 / num2}")

# Number system: 


num = int(input("Enter a number: "))

if num >0:
    print("Positive")
else:
    print("Negative")

# Password Features:

while True:

    password = " "

    if password != "Ram@123":
        password = input("Enter Your password: ")
        print("Invalid username or password , Please try again.")

    else: 
        print("Login successfull")
