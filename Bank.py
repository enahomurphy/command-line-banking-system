import helpers as validator
class BankAccount(object):
    """defininng banlkingclass propeties  """
    def __init__(self, name, acc_no, balance):
        self.name =  name
        self.acc_no = acc_no
        self.balance =  balance
    def save_acc(self):
        self.acc = {"name": self.name, "account_no": self.acc_no, "balance":self.balance}
        return self.acc;

    def deposit(self, amount):
        self.balance += amount
        return self.save_acc();
        return

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -=amount;
            return self.save_acc()

    def balance_inquiry(self):
        return self.balance
