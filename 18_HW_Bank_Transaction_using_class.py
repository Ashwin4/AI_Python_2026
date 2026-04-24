"""
Assigmnet:
----------
welcome to AI bank

enter ur name: 
d-Deposit
w-withdraw
e-exit


choose your option: d
Enter the amount: 10000
Balance after deposit : 20000

choose option--w
enter the amount: 5000
balance after withdraw: 10000

choose option: e

exit

"""
class customer:
    bankname="AI Bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance after deposit is $:",self.balance )

    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient funds cannot perform this operation")
        else:
            self.balance=self.balance-amt
            print("Balance after withdraw is $:",self.balance)


print("Welcome to ",customer.bankname) #Static variable
name=input("Enter your name : ")
c=customer(name)# Object created
while True:
    print("d-for Deposit \n w--for Withdraw \n e-for Exit")
    option=input("Please choose your option ")
    if option=='d' or option=='D':
        amt=float(input("Please enter the amount $"))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input("Please enter a amount $"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for Banking")
        break
    else:
        print("Invalid option.... Please choose the valid option")





        