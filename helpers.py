import sys
import random
"""
creating helper functions for the banking system
"""

"""
validating youser inputs
"""
def validate_user_input(message, data_type, err):
    while True:
        a = raw_input("{}: ".format(message))
        try :
          return  data_type(a)
          break
        except:
          print  (err)
"""
reads account out of the file
"""
def account_reader(account_file):
    acc = open(account_file, "r+")
    if acc.read() == '':
        acc.write('[]')
    acc.seek(0)
    return acc.read()

"""
writes accounts into the file
"""
def account_writer(account_file, value):
    acc = open(account_file, "w")
    acc.write(value);
    account_reader(account_file)
    return
#account_writer("accounts.txt","lihoi4oi4oi4i43")

"""
converts text in the file to an array
"""
def text_to_array(account_file):
    acc = account_reader(account_file)
    new_acc = eval(acc)
    return new_acc

"""
generates a unique account NUMBER
@TODO : add a unique number at the begining of each account number generation eg 345-(generated number)
"""
def acc_no_generator(account_file):
    acc = text_to_array(account_file)
    while True:
        a = random.sample(xrange(1000000000), 1)
        if acc == []:
            return a[0]
        else:
            for i in acc:
                if i['account_no'] != a[0]:
                    return a[0]
                    break;

"""
gets user account and returns  true if found
"""
def get_acc(account_file,acc_no):
    acc = text_to_array(account_file)
    user = None
    for i in acc:
        if i['account_no'] == acc_no:
            user = i
            acc.remove(i)
            account_writer(account_file, '{}'.format(acc))
            break
        else :
            user = False
    return user

"""
gets user accounts and deletes it if found
"""
def close_account(account_file, account_no):
    acc = text_to_array(account_file)
    user = None
    for i in acc:
        if i['account_no']  == account_no:
            acc.delete(i)
            account_writer("accounts.txt",acc)
            user = True
            break;
        else:
            user = False
    return user

"""
returns all accounts info of accounts holder
"""
def get_all_holder(account_file):
    holders = text_to_array(account_file)
    users = None
    if holder == []:
        return users
    else:
        users = []
        for i in holders:
            users.append(i)
    return users

"""
gets user accounts
"""
def get_user_acc(account_file, account_no):
    acc = text_to_array(account_file)
    for i in acc:
        if i["account_no"] == account_no:
            res = i
        else:
            res = False
    return res
