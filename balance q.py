balance=float(input("Enter your account balance : "))
while True:
    if((balance<0) or (balance>2000)):
        print("Invalid account balance. Your account balance should be in the range of 0 and 2000.")
    break
withdraw=int(input("Enter the amount you want to withdraw : "))
if((withdraw<0) or (withdraw>2000) or (withdraw>balance)or(withdraw%5!=0)):
    print(f"{balance:.2f}")
else:
    balance-=(withdraw+0.50)
    print(f"{balance:.2f}")