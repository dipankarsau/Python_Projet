class Atm:
    def __init__(self):
        self.pin = None
        self.balance = 0
        self.menu()

    def menu(self):

        user_input = input("""
        How can I help you?

        1. Press 1 to create PIN
        2. Press 2 to change PIN
        3. Press 3 to check balance
        4. press  4 to withdrawl

        Enter your choice:
        """)

        if user_input == "1":
            self.create_pin()

        elif user_input == "2":
            self.change_pin()

        elif user_input == "3":
            self.check_balance()
        elif user_input=="4":
            self.withdrawl()
        else:
            print("Thank you for using ATM")
            self.exit()

    def create_pin(self):
        user_pin = int(input("Enter your PIN: "))
        self.pin = user_pin

        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance

        print("PIN generated successfully")

        self.menu()

    def change_pin(self):
        old_pin = int(input("Enter your old PIN: "))

        if old_pin == self.pin:
            new_pin = int(input("Enter your new PIN: "))

            self.pin = new_pin

            print("PIN changed successfully")

            self.menu()

        else:
            print("Wrong PIN")

            self.menu()
    def check_balance(self):
        user_pin=int(input("enter your pin :-"))
        if user_pin==self.pin:
            print(f" your balance is {self.balance}")
            self.menu()
        else:
            print(" enter correct pin :-")
            self.menu()
    def withdrawl(self):
        user_pin=int(input(" enter your pin :-4"))
        if user_pin == self.pin:
            amount=int(input(" enter youe amount :-"))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print(f" withdrawl succesfully your remaning amount is {self.balance}")
                self.menu()
            else:
                print(" your balance is infulance")
                self.menu()
    def exit(self):
        print(" please enter a valid number")
        


object = Atm()