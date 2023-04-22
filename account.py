class Account:
    def __init__(self, name: str) -> None:
        '''
        Function to set up the object.
        :param name: Account name.
        '''
        self.__account_name = name
        self.__account_balance = 0
    
    
    def deposit(self, amount: float) -> bool:
        '''
        Function to increase the balance of the account.
        :param amount: How much to increase balance by.
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    
    
    def withdraw(self, amount: float) -> bool:
        '''
        Function to decrease the balance of the account.
        :param amount: How much to decrease balance by.
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    
    def get_balance(self) -> None:
        '''
        Gets the current balance of the account.
        '''        
        return self.__account_balance
    
    
    def get_name(self) -> None:
        '''
        Gets the name listed on the account.
        '''
        return self.__account_name
    
    