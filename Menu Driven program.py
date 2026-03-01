balance = 0.0

def display():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount Deposited")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn")
    else:
        print("Insufficient Balance")

while True:
    print("1.Display Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        display()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        break