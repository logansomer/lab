class Account:
    def __init__(self,name)-> None:
        '''
        Funtion sets up inital objects
        :param name: name of user
        '''
        self.__account_balance = 0.00
        self.__account_name = name
    def deposit(self,amount:float) -> float:
        '''
        Funtion allows user to depsit sed amount into account balance
        :param amount: valuble for inputed number value as float
        :return: True or False (depending on input)
        '''
        if amount <= 0.00:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self,amount:float) -> float:
        '''
        Funtion allows user to withdraw sed amount from account balance
        :param amount: valuble for inputed number value as float
        :return: True or False (depending on input)
        '''
        if amount <= 0.00 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True
    def get_balance(self) -> float:
        '''
        fution returns balance (helps clean up code)
        :return: account balance
        '''
        return self.__account_balance
    def get_name(self) -> str:
        '''
        fution returns name (helps clean up code)
        :return: account name
        '''
        return self.__account_name

