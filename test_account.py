from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('James')
        
    def teardown_method(self):
        del self.a1
        
    def test_init(self):
        assert self.a1.get_name() == 'James'
        assert self.a1.get_balance() == 0
        
    def test_deposit(self, amount):
        self.a1.deposit(self, 100.00)
        assert self.a1.get_balance() == 100.00
        self.a1.deposit(self, 100.00)
        assert self.a1.get_balance() == 200.00
        self.a1.deposit(self, 0)
        assert self.a1.get_balance() == 200.00
        self.a1.deposit(self, -1)
        assert self.a1.get_balance() == 200.00
        
    def test_withdraw(self):
        self.a1.deposit(self, 10.00)
        self.a1.withdraw(self, 0)
        assert self.a1.get_balance() == 0
        self.a1.withdraw(self, -1)
        assert self.a1.get_balance() == 0
        self.a1.withdraw(self, 5.00)
        assert self.a1.get_balance() == 5.00
        self.a1.withdraw(self, 6)
        assert self.a1.get_balance() == 5.00
        self.a1.withdraw(self, 5)
        assert self.a1.get_balance() == 0
        