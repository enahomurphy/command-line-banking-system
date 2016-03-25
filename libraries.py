from Bank import  BankAccount
import helpers as validator
"""
file accounts are been saved
"""
account_file = 'accounts.txt'

"""
creates new banking all_accounts
@TODO : add account type
"""
def new_account():
    acc = validator.text_to_array(account_file)
    Acc_name = validator.validate_user_input("enter your account name", str, "please enter  a valid name")
    Acc_number = validator.acc_no_generator(account_file)
    print "this is your account number {}".format(Acc_number)
    Acc_bal = validator.validate_user_input("enter your initial bal", int, "please enter  valid amount")
    new_acc = BankAccount(Acc_name,Acc_number,Acc_bal )
    user_acc = new_acc.save_acc()
    acc.append(user_acc)
    validator.account_writer(account_file, '{}'.format(acc))
    return user_acc
# validator.acc_no_generator()
"""
deposit certain amounts to user account
"""
def deposit_amount():
    while True:
        acc_no = validator.validate_user_input("enter your account No", int, "please enter  valid account")
        user_acc = validator.get_acc(account_file, acc_no)
        if user_acc == False:
            print "user with that this {} number found".format(acc_no)
        else:
            break
    amount = validator.validate_user_input("enter amount to deposit", int, "please enter  valid amount")
    acc = validator.text_to_array(account_file)
    user = BankAccount(user_acc['name'],user_acc['account_no'],user_acc['balance'] )
    deposit = user.deposit(amount)
    acc.append(deposit)
    validator.account_writer(account_file, '{}'.format(acc))
    print 'successful'
    return user_acc, deposit

"""
withdraws certain amounts to user account
"""
def withdraw_amount():
    while True:
        acc_no = validator.validate_user_input("enter your account No", int, "please enter  valid account")
        user_acc = validator.get_acc(account_file, acc_no)
        if user_acc == False:
            print "user with that this {} number found".format(acc_no)
        else:
            break
    acc = validator.text_to_array(account_file)
    user = BankAccount(user_acc['name'],user_acc['account_no'],user_acc['balance'] )
    while True:
        amount = validator.validate_user_input("enter to withdraw", int, "please enter  valid amount")
        withdrawer = user.withdraw(amount)
        if withdrawer  == False:
            print "You acc balance is {} you cannot withdraw {}".format(user.balance, user.acc['balance'], u)
        else:
            break
    acc.append(withdrawer)
    validator.account_writer(account_file, '{}'.format(acc))
    return  user_acc, withdrawer
#print withdraw_amount()
"""
gets accounts deatils
"""
def account_inquiry():
    while True:
        acc_no = validator.validate_user_input("enter your account No", int, "please enter  valid account")
        user_acc = validator.get_user_achelpsc(account_file, acc_no)
        if user_acc == False:
            print "user with that this {} number found".format(acc_no)
        else:
            break
    return user_acc

def all_accounts():
    holders = validator.text_to_array(account_file)
    users = None
    if holders == []:
        return users
    else:
        users = []
        for i in holders:
            users.append(i)
    return users
#all_accounts()
"""
modifies the user accounts:
@TODO:modification of account type
"""
def modify_account():
    while True:
        acc_no = validator.validate_user_input("enter your account No", int, "please enter  valid account")
        user_acc = validator.get_acc(account_file, acc_no)
        if user_acc == False:
            print "user with that this {} number found".format(acc_no)
        else:
            break
    acc = validator.text_to_array(account_file)
    new_acc = dict(user_acc)
    Acc_name = validator.validate_user_input("enter your new Acc name", str, "please enter  a valid name")
    new_acc['name'] = Acc_name
    acc.append(new_acc)
    validator.account_writer(account_file, '{}'.format(acc))
    return  user_acc, new_acc
"""
closes user accounts --- deletes it completely
"""
def close_account():
    res = None
    while True:
        acc_no = validator.validate_user_input("enter your account No", int, "please enter  valid account")
        while True:
            ques = str.lower(validator.validate_user_input("Aar you sure You want to do this (Yes/No)", str, "please enter (Yes/No)"))
            if ques == "yes":
                res = True
                break
            elif ques == "no":
                res = False
                break
            else:
                print "you must type in (yes/no)"
        if res == False:
            break
        else:
            user_acc = validator.get_acc(account_file, acc_no)
            if user_acc == False:
                print "user with that this {} number found".format(acc_no)
                continue
            else:
                return user_acc
                break
