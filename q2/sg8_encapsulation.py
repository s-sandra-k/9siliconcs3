class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = 0 #Private attribute because of the double uncderscore
        self.__balance = 0.0 #"
        self.set_balance(balance) 
        self.set_account_number(account_number)

        
    def set_account_number(self, account_number): #This is to set the account number, also using the setter method to ensure validation.
        self.__account_number = account_number 
        
    def set_balance(self, balance): #This is to set the balance, also using the setter method.
        if balance < 0:
            print("The balance cannot be a negative input.") #This is to ensure that the balance inputed cannot be a negative number.
        else:
            self.__balance = float(balance)
        
    @property #This is to get the account number using the getter method.
    def account_number(self):
        return self.__account_number
    
    @property #This one on the other hand is to get the balance, also using the getter method.
    def balance(self):
        return self.__balance
    
#Printing the information
if __name__ == "__main__": 
    acc = BankAccount(12345, 1000.0)
    
    print("Account 1")
    print("Account Number:", acc.account_number)
    print("Balance:", acc.balance)
    
    print("\nUpdate balance to -100")
    acc.set_balance(-100)
    print("Account Number:", acc.account_number)
    print("Balance:", acc.balance)    
    
