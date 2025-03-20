from BankOps import *

def main():
    bank=BankingSystem()

    while True:
        print("\n***Enter the choice***")
        print("1.Create account")
        print("2.Deposite amount")
        print("3.Withdraw amount")
        print("4.Display information")
        print("5.Break")
        print("")

        try:
            ch=int(input())
            if(ch==1):
                name=input("Enter the name: ")
                add=input("Enter the address: ")
                deposit=int(input("Enter the amount to deposit: "+"Rs."))

                bank.create_acc(name, add, deposit)

            elif(ch==2):
                amt=int(input("Enter the amount to deposit: "+"Rs."))

                b2=bank.deposit_amt(amt)

            elif(ch==3):
                amt=int(input("Enter the amount to withdraw: "+"Rs."))

                bank.withdraw_amt(amt)

            elif(ch==4):
                b4=bank.display()

            elif(ch==5):
                break
            
            else:
                print("Invali Input")
        except Exception as e:
            print(e)



if __name__ == "__main__":
    main()
