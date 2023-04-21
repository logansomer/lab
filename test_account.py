from pytest import *
from account import *


class Test:
    def setup_method(self):
        self.name1 = Account('john')
    def teardown_method(self):
        del self.name1

    def test_init(self):
        assert self.name1.get_name() == 'john'
        assert self.name1.get_balance() == 0.00
    def test_deposit(self):
        assert self.name1.deposit(0) is False
        assert self.name1.get_balance() == 0.00
        assert self.name1.deposit(-1) is False
        assert self.name1.get_balance() == 0.00
        assert self.name1.deposit(1) is True
        assert self.name1.get_balance() == 1.00


    def test_withdraw(self):
        assert self.name1.withdraw(0) is False
        assert self.name1.get_balance() == 0.00
        assert self.name1.withdraw(-1) is False
        assert self.name1.get_balance() == 0.00
        assert self.name1.deposit(3) is True
        assert self.name1.get_balance() == 3.00
        assert self.name1.withdraw(2) is True
        assert self.name1.get_balance() == 1.00




